from connect import db,mydb
query="drop database school"
db.execute(query)
t=db.fetchall()
for i in t:
    print(t)