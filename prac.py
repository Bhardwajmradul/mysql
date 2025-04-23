from connect import db,mydb
query="select * from students"
db.execute(query)
print(db.description)
# for record in db.fetchall():
#     print( record)
# query="select * from subjects"
# db.execute(query)
# query="select * from marks"
# for record in db.fetchall():
#     print( record)
# db.execute(query)
# for record in db.fetchall():
#     print( record)

