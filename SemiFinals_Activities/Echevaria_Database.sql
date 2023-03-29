CREATE DATABASE EnrollmentDB;

USE EnrollmentDB;

CREATE TABLE Professor(
	ProfessorID INT PRIMARY KEY,
	LastName VARCHAR(255) NOT NULL,
    FirstName VARCHAR(255) NOT NULL,
    MidName VARCHAR(255),
    ProfRank VARCHAR(255)
);

CREATE TABLE Section(
	SectionCode INT,
    SchoolYear VARCHAR(10),
    Semester INT,
    SubjCode INT NOT NULL,
    SubjDay VARCHAR(255) NOT NULL,
    SubjTime TIME NOT NULL,
    Room VARCHAR(255) NOT NULL,
    ProfessorID INT,
    PRIMARY KEY (SectionCode, SchoolYear, Semester),
    FOREIGN KEY (ProfessorID) REFERENCES professor(ProfessorID)
);

CREATE TABLE Course(
	CourseCode INT PRIMARY KEY,
    CourseName VARCHAR(255) NOT NULL   
);

CREATE TABLE Municipality(
	ZipCode INT PRIMARY KEY,
    Town VARCHAR(255)
);
CREATE TABLE Student(
	StudentNo INT PRIMARY KEY,
    LastName VARCHAR(255) NOT NULL,
    FirstName VARCHAR(255) NOT NULL,
    MidName VARCHAR(255),
    BirthDate DATE NOT NULL,
    CourseCode INT,
    Email VARCHAR(255) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    RatePerUnit FLOAT NOT NULL,
    ZipCode INT,
    FOREIGN KEY (CourseCode) REFERENCES Course(CourseCode),
    FOREIGN KEY (ZipCode) REFERENCES Municipality(ZipCode)
);

CREATE TABLE Enrollment(
	StudentNo INT,
    SectionCode INT,
    SchoolYear VARCHAR(10),
    Semester INT,
    FOREIGN KEY (StudentNo) REFERENCES Student(StudentNo),
    FOREIGN KEY (SectionCode, SchoolYear, Semester) REFERENCES Section(SectionCode, SchoolYear, Semester)
);