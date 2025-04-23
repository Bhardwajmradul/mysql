from connect import db,mydb
query="drop database stu"
db.execute(query)
t=db.fetchall()
for i in t:
    print(t)