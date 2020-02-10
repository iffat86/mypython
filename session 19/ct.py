import sqlite3
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname,'test.db')

conn = sqlite3.connect(filename)
print('Opened database successfully')

cur = conn.cursor()

mylist = [(100,"Sara",23,"karachi",34000.0),(101,"zara",20,"karachi",30000.0),
(102,"haya",29,"karachi",34500.0),
(103,"Sara",23,"karachi",34000.0),
(109,"Sara",23,"karachi",34000.0),
(104,"Sara",23,"karachi",34000.0),
(110,"Sara",23,"karachi",34000.0),
(105,"Sara",23,"karachi",34000.0),
(106,"Sara",23,"karachi",34000.0),
(107,"Sara",23,"karachi",34000.0),
(108,"Sara",23,"karachi",34000.0)]

for x in mylist:

    cur.execute('INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)VALUES(?,?,?,?,?)',(x[0],x[1],x[2],x[3],x[4]))

conn.commit()
conn.close()