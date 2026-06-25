DROP TABLE IF EXISTS teachers;
DROP TABLE IF EXISTS classes;
CREATE TABLE teachers (
    teacher_id INT PRIMARY KEY,
    teacher_name VARCHAR(50),
    subject VARCHAR(30),
    experience_years INT,
    city VARCHAR(50)
);
CREATE TABLE classes (
    class_id INT PRIMARY KEY,
    teacher_id INT,
    class_name VARCHAR(50),
    section CHAR(1),
    students_count INT,
    room_no VARCHAR(10)
);
INSERT INTO teachers VALUES
(1, 'Mr. Kumar', 'Maths', 10, 'Chennai'),
(2, 'Ms. Priya', 'Science', 7, 'Madurai'),
(3, 'Mr. John', 'English', 5, 'Coimbatore');
INSERT INTO classes VALUES
(101, 1, '10th Std', 'A', 40, 'R1'),
(102, 1, '9th Std', 'B', 38, 'R2'),
(103, 2, '8th Std', 'A', 42, 'R3'),
(104, 3, '7th Std', 'C', 35, 'R4'),
(105, 4, '6th Std', 'A', 30, 'R5');
SELECT t.teacher_name, c.class_name
FROM teachers t
INNER JOIN classes c
ON t.teacher_id = c.teacher_id;
SELECT t.teacher_name, c.class_name
FROM teachers t
LEFT JOIN classes c
ON t.teacher_id = c.teacher_id;
SELECT t.teacher_name, c.class_name
FROM teachers t
RIGHT JOIN classes c
ON t.teacher_id = c.teacher_id;
SELECT t.teacher_name, c.class_name
FROM teachers t
FULL OUTER JOIN classes c
ON t.teacher_id = c.teacher_id;
SELECT teacher_name, class_name
FROM teachers
NATURAL JOIN classes;
SELECT t.teacher_name, c.class_name
FROM teachers t
CROSS JOIN classes c;