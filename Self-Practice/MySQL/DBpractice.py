import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Johnleo1152003.",
    database="enrollmentDB"  # Can only use this if there is a DB created
)

cursor = db.cursor()


def create_table():
    cursor.execute(
        """CREATE TABLE Person(
            personID int PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(50),
            age int,
            birthday date)""")


def insert_table():
    cursor.execute(
        """INSERT INTO Person(name, age) VALUES (%s,%s)""", ("tim", 19))
    db.commit()  # Saves the inserted values


test_input = input("Enter table name: ")
selection_input = input("Would you like to select all or a specific column? (Type 'all' or name of column): ")
if selection_input.lower() == "all":
    selection = "*"
else:
    selection = selection_input
cursor.execute(f"SELECT {selection} FROM {test_input}")

for x in cursor:
    print(x)
