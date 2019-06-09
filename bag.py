#链接数据库
import pandas as pd
import pyodbc

connection = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};Server=localhost;database=data;uid=sumiya;pwd=s1999211')
query = 'select * from dbo.Sheet1$'

df1 = pd.read_sql_query(query,connection)
print(df1.head(8))
