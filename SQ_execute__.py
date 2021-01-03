import sqlite3

conn = sqlite3.connect("E:\代码\Python\addressBook.db")
cur = conn.cursor()               #创建游标
cur.execute('''INSERT INTO addressList(name , sex , phon , QQ , address) VALUES('王小丫' ,  '女' ,  '13888997011' ,  '66735' ,  '北京市' )''')
cur.execute('''INSERT INTO addressList(name, sex, phon, QQ, address) VALUES('李莉', '女', '15808066055', '675797', '天津市')''')
cur.execute('''INSERT INTO addressList(name, sex, phon, QQ, address) VALUES('李星草', '男', '15912108090', '3232099', '昆明市')''')
conn.commit()                      #提交事务，把数据写入数据库
conn.close()
