import sqlite3
conn = sqlite3.connect("D:\\test.db")
c = conn.cursor()
c.execute('''CREATE TABLE stocks(date text, trans text, symbol text, qty real, price real)''')
c.execute("""INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)""")
conn.commit()
c.close()

conn.row_factory = sqlite3.Row
c = conn.cursor()
c.execute('SELECT * FROM stocks')
r = c.fetchone()
print(type(r))
print(tuple(r))
print(r[2])
print(r.keys())
print(r['qty'])
for field in r:
    print(field)
