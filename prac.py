from connect import db,mydb
db.execute("select * from Marks as m right join Student as s on m.Rollno =s.Rollno where m.Rollno is null")


l=db.fetchall()
for record in l:
    print( record)