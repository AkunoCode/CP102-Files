# Echevaria, John Leo D.
import mysql.connector

class EnrollmentDB:
    def __init__(self):
        self.db = mysql.connector.connect(host='localhost', user='root', passwd='', database='enrollmentdb')
        
        self.cursor = self.db.cursor()
    
    def add(self):
        print("Type in the Subject Info:")
        subjectcode = input("Enter Subject Code: ")
        subjectname = input("Enter Subject Name: ")
        units = input("Enter Subject Units: ")
        self.cursor.execute("INSERT INTO subject VALUES (%s,%s,%s)",(subjectcode,subjectname,units))
        
        self.db.commit()
    
    def search(self):
        subjectcode = input("Enter Subject Code: ")
        
        self.cursor.execute("SELECT * FROM subject WHERE subjectcode = %s",(subjectcode,))
        results = self.cursor.fetchall()
        for result in results:
            print(f"Subject Code: {result[0]}")
            print(f"Subject Name: {result[1]}")
            print(f"Subject Units: {result[2]}")

test = EnrollmentDB()
while True:
    print("[1] Add Subject")
    print("[2] Search Subject")
    print("[3] Exit")
    choice = int(input("Choose an Action: "))
    
    if choice == 1:
        test.add()
    elif choice == 2:
        test.search()
    elif choice == 3:
        break
    else:
        print("Invalid Choice")
            






