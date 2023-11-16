# mdx_to_pd

mdx to pd is a Python library for retrieving data from Microsoft Analytics Services OLAP cube using the mdx query Returned outcome comes in the pandas dataframe for further data processing.
Works also behind the corporate proxy.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install mdx_to_pd.
In order for mdx_to_pd to work it is necessary to have Microsoft.PowerBI.AdomdClient.dll.
Package works on Windows only!

```bash
pip install mdx-to-pd
```

## Usage

```python
from mdx_to_pd import mdx_retriever


connection = "Data Source=https://biserver.company.com/database/;Catalog=Model;"
query = """
        SELECT NON EMPTY [Measures].[Order Count] ON COLUMNS,
        NON EMPTY ([Markets].[Country].[Country]) ON ROWS
        FROM [OLAP_CUBE]
        """
# returns pd.DataFrame()

df = mdx_retriever(query, connection)

# mdx or dax query can be provided
# returns df based on mdx query with column names with whitespace replaced by '_'
# to return own column whitespace replacement string, add parameter 

df = mdx_retriever(query, connection,'-')

# in case of error due to missing Microsoft.PowerBI.AdomdClient.dll
# please follow prompts in terminal.
# package expects file located in 
# c:\Program Files\Microsoft Power BI Desktop\bin\ but path is not
# existing it will search for the file on c: drive and will suggest to add this as parameter

df = mdx_retriever(query, 
                   connection,
                   '-',
                   'c:\\alternative_path_to\\Microsoft.PowerBI.AdomdClient.dll')

# all options:
mdx_retriever(
     query: str, # mdx query
     conn:str, # connection to OLAP CUBE,
     whitespace_replacer: str #optional replacement string for column whitespaces
     alternative_dll_path: str #optional alternative path to Microsoft.PowerBI.AdomdClient.dll
)

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)