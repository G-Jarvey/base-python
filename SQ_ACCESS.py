#建立数据库连接
import win32com.client   
conn = win32com.client.Dispatch(r'ADODB.Connection')   
DSN = 'PROVIDER=Microsoft.Jet.OLEDB.4.0;DATA SOURCE=C:/MyDB.mdb;'   
conn.Open(DSN)

#打开记录集
rs = win32com.client.Dispatch(r'ADODB.Recordset')   
rs_name = 'MyRecordset'#表名   
rs.Open('[' + rs_name + ']', conn, 1, 3)
