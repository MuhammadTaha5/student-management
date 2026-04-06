CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    registration_number VARCHAR(50) UNIQUE,
    subjects TEXT,
    cgpa FLOAT
);

INSERT INTO students (first_name,last_name,registration_number,subjects,cgpa)
VALUES
('Ali','Khan','2022-CS-101','OOP,Database,Networks',3.45),
('Sara','Ahmed','2022-CS-102','AI,ML,Database',3.80);
