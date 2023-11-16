import pandas as pd
import os
import clr
from alive_progress import alive_bar
from pathlib import Path

def mdx_retriever(query: str,
                  olap_connection_string: str,
                  space_replacer='_',
                  adomd_dll='c:\\Program Files\\Microsoft Power BI Desktop\\'
                            'bin\\Microsoft.PowerBI.AdomdClient.dll'):

    # query: MDX QUERY eg. SELECT
    #                           Measures.[MEASURE]
    #                      ON COLUMNS,
    #                           [TABLE].[MEMBER.[MEMBER]
    #                       ON ROWS
    #                      FROM[Database]
    #
    # olap_connection_string: olap database connection strin e.g.
    #        Data Source=https://biserver.domain.com/version/; Catalog=version;
    #
    # space_replacer: string to replace the whitespaces on column names
    #                 default = '_', use ' ' to keep as source data
    #
    # adomd_dll: path to Microsoft.PowerBI.AdomdClient.dll file
    # default is set for standard path for PBI Desktop installation:
    #   c:\\Program Files\\Microsoft Power BI Desktop\\bin\\
    #   if not found function will search the client to find the file and suggests the path

    # process to check of adomd_dll exists and find it if it doesn't
    adomd_dll = Path(adomd_dll)
    if adomd_dll.is_file():
        # print('default AdomdClient file found!')
        pass
    else:
        adomd_dll = ''
        print('Microsoft.PowerBI.AdomdClient.dll not at expected path, searching for the file...')
        for root, dirs, files in os.walk('c:\\'):
            for name in files:
                if name == 'Microsoft.PowerBI.AdomdClient.dll':
                    adomd_dll = os.path.abspath(os.path.join(root, name))
                    if 'Power BI' in adomd_dll:
                        print('AdomdClient found, please use the path in function call,'
                              ' preferably the one installed with Power BI!')
                        print(adomd_dll)
                        break
                    else:
                        continue
            else:
                continue
            break
    #print(adomd_dll)
    if len(str(adomd_dll)) == 0:
        print('You are missing Microsoft.PowerBI.AdomdClient.dll. Please install Power BI desktop')
        df = pd.DataFrame()
        return df  # empty df returned if no adomd_dll is found

    clr.AddReference(str(adomd_dll))
    clr.AddReference("System.Data")
    # proxy workaround for adomd access via clr
    clr.AddReference("System.Net")
    from System.Net import ServicePointManager, SecurityProtocolType

    ServicePointManager.SecurityProtocol = SecurityProtocolType.Ssl3 | SecurityProtocolType.Tls12 | SecurityProtocolType.Tls11 | SecurityProtocolType.Tls
    from Microsoft.AnalysisServices.AdomdClient import AdomdConnection, AdomdDataAdapter
    conn = AdomdConnection(olap_connection_string)

    if len(query) == 0:
        print("No query entered! Please provide a mdx query.")
    data = []
    conn.Open()  # opens connection to OLAP CUBE
    mdx_query = query
    cmd = conn.CreateCommand()
    cmd.CommandText = (''.join(mdx_query))
    print(f"Getting data from OLAP cube, this may take a while ...")
    reader = cmd.ExecuteReader()
    SchemaTable = reader.GetSchemaTable()
    numCol = SchemaTable.Rows.Count  # same as DataReader.FieldCount
    # column names workaround and beatification:
    columns_names = []
    for i in range(numCol):
        columns_names.append(reader.GetName(i))
    measures_counter = 0
    for i in columns_names:
        if '[Measures]' in i:
            measures_counter += 1
    dimensions_list = []
    measures_list = []
    if "select" in query.lower():
        print('MDX query was provided')
        for dimension_name in columns_names[0:len(columns_names) - measures_counter]:
            column_caption = dimension_name[dimension_name.find('].[', dimension_name.find('].[') + 1) + 3:].replace(
                '].[MEMBER_CAPTION]', '').replace(' ', space_replacer)
            dimensions_list.append(column_caption)
        for measure_name in columns_names[len(columns_names) - measures_counter:]:
            column_caption = measure_name.replace('[Measures].[', '').replace(']', '').replace(' ', space_replacer)
            measures_list.append(column_caption)
    else:
        print('DAX query was provided')
        dimensions_list = [item.split('[')[-1].rstrip(']').replace(' ', space_replacer) for item in columns_names]
    columns_names = dimensions_list + measures_list
    print(f"data capture loop started ...")
    # data reader and inputs to Pandas df
    with alive_bar() as bar:
        while reader.Read():
            row = []
            for j in range(numCol):
                try:
                    row.append(reader[j].ToString())
                except:
                    row.append(reader[j])
            data.append(row)
            bar()
    try:
        conn.Close()
        #print("connection closed")
    except:
        pass
    df = pd.DataFrame(data)
    df.columns = columns_names
    return df


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(__name__)
