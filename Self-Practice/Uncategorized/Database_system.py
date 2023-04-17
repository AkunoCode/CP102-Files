import mysql.connector
from mysql.connector import errorcode
import os
import time

class BookstoreDB:
    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'Johnleo1152003.'
        )
        self.cursor = self.db.cursor()

        try:
            self.cursor.execute("USE bookstoredb")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist...")
                time.sleep(2)
                os.system('cls')
                print("Creating Database...")
                self.createdb()
                time.sleep(2)
                os.system('cls')
                print("Database Created...")
                time.sleep(2)
                os.system('cls')
            else:
                print(err)
                self.db.rollback()

    def createdb(self):
        self.cursor.execute("CREATE DATABASE bookstoredb")

        self.cursor.execute("USE bookstoredb")

        self.cursor.execute("""CREATE TABLE books(
        book_id INT PRIMARY KEY AUTO_INCREMENT,
        title VARCHAR(255),
        author VARCHAR(255),
        publication_date DATE,
        price FLOAT
        )""")

        self.db.commit()
    
    def add_book(self, title, author, publication, price):
        try:
            self.cursor.execute("INSERT INTO books(title, author, publication_date, price) VALUES (%s,%s,%s,%s)",(title,author,publication,price))

            self.db.commit()
        except mysql.connector.Error as err:
            print(err)
            self.db.rollback()
    
    def view(self):
        print("Here are the available books:\n")
        self.cursor.execute("SELECT * FROM books")
        books = self.cursor.fetchall()
        for book in books:
            print(f"BookID: {book[0]}")
            print(f"Book Title and Author: {book[1]} ({book[2]})")
            print(f"Publication Date: {book[3]}")
            print(f"Price: {book[4]}")
            print()
    
    def delete(self,bookid):
        try:
            self.cursor.execute("DELETE FROM books WHERE book_id = %s", (bookid,))
            self.db.commit()
        except mysql.connector.Error as err:
            # If book_id does not exist
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Book ID does not exist")
            else:
                print(err)
                self.db.rollback()
    
    def edit(self,bookid,title,author,publication,price):
        try:
            self.cursor.execute("UPDATE books SET title = %s, author = %s, publication_date = %s, price = %s WHERE book_id = %s",(title,author,publication,price,bookid))
            self.db.commit()
        except mysql.connector.Error as err:
            # If book_id does not exist
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Book ID does not exist")
            else:
                print(err)
                self.db.rollback()

os.system('cls')
nbs = BookstoreDB()
while True:
    os.system('cls')
    print("Welcome to Charity Books where we sell books for a cause.")
    print("[1] Donate Book")
    print("[2] Delete Book")
    print("[3] Edit Book")
    print("[4] View Books")

    choice = input("Choose an action to perform: ")
    if choice ==  "1":
        os.system('cls')
        print("Input the info of the book you're donating.\n")
        title = input("Title: ")
        author = input("Author: ")
        publication = input("Publication Date (YYYY-MM-DD): ")
        price = float(input("Selling Price: "))
        nbs.add_book(title,author,publication,price)
        print("\nBook Successfully Donated!")
        time.sleep(2)
        os.system('cls')
        nbs.view()
        input("Press Enter to Continue...")
    elif choice == "2":
        os.system('cls')
        nbs.view()
        bookid = int(input("Enter the Book ID of the book you want to delete: "))
        nbs.delete(bookid)
        print("\nBook Successfully Deleted!")
        time.sleep(2)
        os.system('cls')
        nbs.view()
        input("Press Enter to Continue...")
    elif choice == "3":
        os.system('cls')
        nbs.view()
        bookid = input("Enter the Book ID of the book you want to edit: ")
        title = input("Title: ")
        author = input("Author: ")
        publication = input("Publication Date (YYYY-MM-DD): ")
        price = float(input("Selling Price: "))
        nbs.edit(bookid,title,author,publication,price)
        print("\nBook Successfully Edited!")
        time.sleep(2)
        os.system('cls')
        nbs.view()
        input("Press Enter to Continue...")
    elif choice == "4":
        os.system('cls')
        nbs.view()
        input("Press Enter to Continue...")
    else:
        print("Invalid Input")
        time.sleep(2)
        os.system('cls')


