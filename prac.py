from connect import db,mydb
query=["select * from Student","select * from Subject","select * from Marks","select * from Employee","select * from Teacher"]
for q in query:
    db.execute(q)
    print(q)
    for i in db.fetchall():
        print(i)
    print
mydb.commit()
# ('Mathematics', 1, 45),         -- Mr. Sharma (40000)
# ('Science', 2, 48),             -- Ms. Verma (39000)
# ('English', 3, 50),             -- Mrs. Kapoor (42000)
# ('History', 4, 30),             -- Mr. Sinha (38500)
# ('Geography', 5, 40),           -- Mrs. Rao (41000)
# ('Computer', 6, 35),            -- Ms. Das (39500)
# ('Digital Logics', 7, 41),      -- Mr. Sharma (40500)
# ('Biology', 8, 40),             -- Ms. Verma (39800)
# ('Literature', 9, 52),          -- Mrs. Kapoor (43000)
# ('Civics', 10, 23),             -- Mr. Sinha (37000)
# ('Economics', 11, 34),          -- Mrs. Rao (41500)
# ('DBMS', 12, 45);  