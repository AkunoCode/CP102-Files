CREATE DATABASE UniversityDB;

CREATE TABLE Students(
	Student_ID INT PRIMARY KEY,
    Last_Name VARCHAR(255) NOT NULL,
    First_Name VARCHAR(255) NOT NULL,
    Mid_Name VARCHAR(255),
    Student_Email VARCHAR(255) NOT NULL
);

CREATE TABLE Courses(
	Course_ID INT PRIMARY KEY,
    Course_Title VARCHAR(255) NOT NULL,
    Credit_Hours INT NOT NULL
);

CREATE TABLE Enrollments(
	Enrollment_ID INT PRIMARY KEY,
    Student_ID INT NOT NULL,
    Course_ID INT NOT NULL,
    Semester INT NOT NULL,
    FOREIGN KEY (Student_ID) REFERENCES Students(Student_ID),
    FOREIGN KEY (Course_ID) REFERENCES Courses(Course_ID)
);

ALTER TABLE Students
ADD Student_GPA FLOAT;

ALTER TABLE Enrollments
ADD Final_Grade VARCHAR(2);

CREATE TABLE Professors(
	Professor_ID INT PRIMARY KEY,
    Last_Name VARCHAR(255),
    First_Name VARCHAR(255),
    Mid_Name VARCHAR(255),
    Department VARCHAR(255),
    Office_Location VARCHAR(255)
);

ALTER TABLE Courses
ADD ProfessorID INT,
ADD FOREIGN KEY (ProfessorID) REFERENCES professors(Professor_ID);



