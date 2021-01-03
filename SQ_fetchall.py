#使用fetchall()读取数据：

import sqlite3

conn = sqlite3.connect('D:/addressBook.db')
cur = conn.cursor()
cur.execute('SELECT * FROM addressList')
li = cur.fetchall()                  #返回所有查询结果
for line in li:
    for item in line:
        print(item, end=' ')
    print()
conn.close()
