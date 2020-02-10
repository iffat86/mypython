import sqlite3
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname,'test.db')

conn = sqlite3.connect(filename)
print('Opened database successfully')

cur = conn.cursor()
"""cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES(1,'Paul',32,'Calofornia',20000.0)")
cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES(2,'Paul',?,?,20000.0)",(32,'Texas'))

conn.commit()
conn.close()"""


cur.execute("UPDATE COMPANY set SALARY = 25000.0 where ID = 1")
print("operation done successfully")
conn.commit()


cur.execute("SELECT id,name,address,salary from COMPANY")
for row in cur:
    print('ID =', row[0])
    print('NAME =', row[1])
    print('ADDRESS =', row[2])
    print('SALARY =', row[3], "\n")

print("operation done")

cur.execute("DELETE from COMPANY  where ID = 2;")
conn.commit()
print("total number of rows deleted :", conn.total_changes)
conn.close()

