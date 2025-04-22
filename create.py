from connect import db,mydb
query="select * from subject"
db.execute(query)
l=db.fetchall()
# mydb.commit()
print(l)