#使用直接创建的序列作为SQL语句的参数：

import sqlite3

persons = [("Hugo", "Boss"), ("Calvin", "Klein") ]
conn = sqlite3.connect(":memory:")
# 创建表
conn.execute("CREATE TABLE person(firstname, lastname)")
# 插入数据
conn.executemany("INSERT INTO person(firstname, lastname) VALUES (?, ?)", persons)
# 显示数据
for row in conn.execute("SELECT firstname, lastname FROM person"):
    print(row)
print("I just deleted", conn.execute("DELETE FROM person").rowcount, "rows")
