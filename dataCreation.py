from connect import db,mydb
query='''create database stu;use stu;
    CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    class VARCHAR(10)
);

INSERT INTO Students VALUES
(1, 'Alice', 14, '8A'), (2, 'Bob', 15, '9B'), (3, 'Charlie', 13, '8A'),
(4, 'David', 14, '9A'), (5, 'Eva', 15, '9B'), (6, 'Frank', 14, '8B'),
(7, 'Grace', 13, '8A'), (8, 'Hannah', 14, '9B'), (9, 'Ian', 15, '9A'),
(10, 'Jane', 13, '8A'), (11, 'Kevin', 14, '8B'), (12, 'Lily', 14, '9A'),
(13, 'Mike', 15, '9B'), (14, 'Nina', 14, '9A'), (15, 'Oscar', 13, '8B'),
(16, 'Pia', 14, '8A'), (17, 'Quinn', 15, '9B'), (18, 'Rita', 14, '9A'),
(19, 'Steve', 13, '8A'), (20, 'Tina', 14, '8B');'''
db.execute(query,multi=True)
mydb.commit()
