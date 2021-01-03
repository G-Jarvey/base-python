import sqlite3

# 自定义Python函数
def getLen(s):
    return len(s)

# 在内存中创建临时数据库
conn = sqlite3.connect(":memory:")

# 创建可在SQL调用的函数
conn.create_function("getLen", 1, getLen)

# 创建数据表并插入测试数据
conn.execute("create table test (作家 text, 作品 text, 人物 text)")
conn.execute("insert into test values('曹雪芹', '红楼梦', '贾宝玉')")
conn.execute("insert into test values('罗贯中', '三国演义', '曹操')")
conn.execute("insert into test values('施耐庵', '水浒传', '宋江')")
conn.execute("insert into test values('吴承恩', '西游记', '菩提老祖')")
conn.execute("insert into test values('吴承恩', '西游记', '唐僧')")

# 在查询结果中按照“人物”字段的字符个数排序
sql = "select * from test order by getLen(人物)"
for row in conn.execute(sql):
    print(row)

#关闭内存数据库
conn.close()
