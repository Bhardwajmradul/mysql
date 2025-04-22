from connect import db, mydb

# Step 1: Create database
db.execute("CREATE DATABASE IF NOT EXISTS stu")

# Step 2: Select the database
db.execute("USE stu")

# Step 3: Now run the remaining multi-statement SQL
query = '''
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
(19, 'Steve', 13, '8A'), (20, 'Tina', 14, '8B');

CREATE TABLE Subjects (
    subject_id INT PRIMARY KEY,
    subject_name VARCHAR(50),
    teacher VARCHAR(50)
);

INSERT INTO Subjects VALUES
(101, 'Maths', 'Mr. Sharma'),
(102, 'Science', 'Ms. Verma'),
(103, 'English', 'Mrs. Kapoor'),
(104, 'History', 'Mr. Sinha'),
(105, 'Computer', 'Ms. Das'),
(106, 'Geography', 'Mrs. Rao');

CREATE TABLE Marks (
    student_id INT,
    subject_id INT,
    marks INT,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id)
);

INSERT INTO Marks VALUES
(1, 101, 85), (1, 102, 78), (1, 103, 91),
(2, 101, 76), (2, 104, 82),
(3, 105, 88), (3, 106, 74),
(4, 101, 90), (4, 102, 84), (4, 103, 89),
(5, 104, 67), (5, 105, 73),
(6, 101, 55), (6, 106, 60),
(7, 102, 91), (7, 103, 78),
(8, 101, 83), (8, 104, 77),
(9, 105, 65), (9, 106, 80),
(10, 102, 86), (10, 103, 90),
(11, 101, 70), (11, 105, 79),
(12, 106, 85), (12, 104, 88),
(13, 103, 92), (13, 101, 81),
(14, 102, 76), (14, 104, 69),
(15, 105, 74), (15, 106, 66),
(16, 101, 88), (16, 102, 81),
(17, 103, 85), (17, 104, 89),
(18, 105, 77), (18, 106, 83),
(19, 101, 62), (19, 103, 59),
(20, 104, 91), (20, 106, 87);
'''
# # Execute the rest with multi=True
for result in db.execute(query, multi=True):
    pass


mydb.commit()
