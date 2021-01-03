#在sqlite3连接中创建并调用自定义函数
import sqlite3
import hashlib

# 自定义Python函数
def md5sum(t):
    return hashlib.md5(t).hexdigest()

# 在内存中创建临时数据库
conn = sqlite3.connect(":memory:")
# 创建可在SQL调用的函数，其中第二个参数表示函数的参数个数
conn.create_function("md5", 1, md5sum)
cur = conn.cursor()
# 在SQL语句中调用自定义函数
cur.execute("select md5(?)", ["中国山东烟台".encode()])
print(cur.fetchone()[0])
