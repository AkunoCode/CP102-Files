-- Inserting Values into the Table
INSERT INTO Course VALUES
('BSCS','Bachelor of Science in Computer Science'),
('BSIT','Bachelor of Science in Information Technology'),
('BSEMC','Bachelor of Science in Electronics Media Computing'),
('BSIS','Bachelor of Science in Information Security'),
('BSCE','Bachelor of Science in Computer Engineering'),
('BSA','Bachelor of Science in Architecture');

SELECT * FROM Course;

INSERT INTO municipality VALUES
('4302','Pagbilao');

INSERT INTO student VALUES
('A22-34233','Echevaria','John Leo','Dimacali','2003-11-05','BSCS','echevariajohnleo@gmail.com','Berana','2000','4302');

SELECT 
	StudentNo as 'Student ID',
    concat(FirstName, ' ', left(MidName, 1), '. ', LastName) as 'Student Name',
    BirthDate,
    CourseCode,
    Email,
    Address,
    RatePerUnit,
    student.ZipCode,
    municipality.town as 'Home Town'
FROM student
JOIN municipality ON student.ZipCode = Municipality.ZipCode;

-- Updating Values

-- Deleting Column
DELETE FROM Course WHERE CourseCode = 'BSA';

-- Retrieve Records
SELECT StudentNo as "Student ID", concat(FirstName,' ',left(MiddleName,1),'. ',LastName) as 'Student Name' FROM student