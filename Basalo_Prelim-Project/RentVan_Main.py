import sys
import time
import os
import re

def main_menu():
    """Welcomes the user and displays the main menu of the program."""
    while True:
        os.system("cls")
        print(
            "\nWelcome to Basalo's Van Rental Service!\n\n"
            "What would you like to do?\n"
            "1. Rent a Van\n"
            "2. View Receipt\n"
            "3. View Transactions\n"
            "4. Exit\n"
        )
        choice = input("Enter your choice: ")
        if choice == "1":
            rent_van()
            break
        elif choice == "2":
            view_receipt()
            break
        elif choice == "3":
            view_transactions()
            break
        elif choice == "4":
            sys.exit()
        else:
            print("Invalid Input!")
            time.sleep(2)

def rent_van():
    """Displays the van capacity and price and asks the user to input 
    their information and the van they want to rent."""
    
    while True:
        os.system("cls")
        print("Here are the available vans and their base prices:\n")
        print("1. Mini Van (5 persons)\t\t\u20B15,000")
        print("2. Regular Van (10 persons)\t\u20B18,000")
        print("3. Passenger Van (15 persons)\t\u20B110,000")

        choice = input("\nEnter your choice: ")
        if choice == "1":
            van_type = "Mini Van"
            van_capacity = 5
            base_price = 5000
            break
        elif choice == "2":
            van_type = "Van"
            van_capacity = 10
            base_price = 8000
            break
        elif choice == "3":
            van_type = "Passenger Van"
            van_capacity = 15
            base_price = 10000
            break
        else:
            print("Invalid Input!")
            time.sleep(2)
    
    while True:
        os.system("cls")
        print(f"You have chosen a {van_capacity} person {van_type}.")
        print("There will be a \u20B1500 fee for every day that you rent the van.\n")
        while True:
            days = int(input("How many days would you like to rent the van?: "))
            if days <= 0:
                print("Invalid Input!")
                time.sleep(2)
            else:
                price = base_price + (days * 500)
                break
        while True:
            os.system("cls")
            print(f"\nThe total price for renting the {van_type} for {days} days is \u20B1{price:,}.")
            choice = input("Would you like to continue? (Y/N) ")
            if choice.upper() == "Y":
                break
            elif choice.upper() == "N":
                main_menu()
                break
            else:
                print("Invalid Input!")
                time.sleep(2)
        break
    
    while True:
        os.system("cls")
        print("Please enter your information.")
        name = input("Name: ")
        
        contact_number = input("Contact Number: ")
        validate = re.search(r"^(09|\+639)\d{9}$", contact_number)
        if validate == None:
            print("Invalid Input!")
            time.sleep(2)
            continue
        
        email = input("Email: ")
        validate = re.search(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email)
        if validate == None:
            print("Invalid Input!")
            time.sleep(2)
            continue
        
        address = input("Address: ")
        date = input("When would you like to rent the van? (mm/dd/yyyy): ")
        validate = re.search(r"^(0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])/\d{4}$", date)
        if validate == None:
            print("Invalid Input!")
            time.sleep(2)
            continue
        
        os.system("cls")
        print("Please confirm your information.")
        print(f"Name: {name}\nContact Number: {contact_number}\nEmail: {email}\nAddress: {address}")
        choice = input("Is this correct? (Y/N) ")
        if choice.upper() == "Y":
            write_receipt(name, contact_number, email, address, van_type, days, price, date)
            record_transaction(name, contact_number, email, address, van_type, days, price, date)
            break
        elif choice.upper() == "N":
            continue
        else:
            print("Invalid Input!")
            time.sleep(2)
    
    while True:
        os.system("cls")
        print("Thank you for renting with us!")
        choice = input("Would you like to rent another van? (Y/N) ")
        if choice.upper() == "Y":
            rent_van()
            break
        elif choice.upper() == "N":
            main_menu()
            break
        else:
            print("Invalid Input!")
            time.sleep(2)


def write_receipt(name, contact_number, email, address, van_type, days, price, date):
    """Writes the receipt of the user in a text file."""
    with open(f"{name.split()[-1]}_{date.replace('/','-')}_Receipt.txt", "w", encoding='utf-8') as file:
        receipt = "--------------------OFFICIAL RECEIPT--------------------\n"
        receipt += f"Name: {name}\nContact Number: {contact_number}\nEmail: {email}\nAddress: {address}\nVan Type: {van_type}\nDays: {days}\nTotal Price: {price}\nRent Date: {date}\n"
        receipt += "\nCalculations:\n"
        receipt += f"Base Price: \u20B1{price - (days * 500):,}\n"
        receipt += f"Additional Fee: \u20B1{days * 500:,}\n"
        receipt += f"Total Price: \u20B1{price:,}\n"
        receipt += "--------------THANK YOU FOR RENTING WITH US--------------\n"
        file.write(receipt)

def record_transaction(name, contact_number, email, address, van_type, days, price, date):
    """Records the transactions in a csv file."""
    with open("Transactions.csv", "a") as file:
        file.write(f"{name},{contact_number},{email},'{address.replace(',',' ')}',{van_type},{days},{price},{date}\n")

def view_receipt():
    """Displays the receipt of the user."""
    while True:
        os.system("cls")
        print("Please enter your name.")
        name = input("Name: ")
        date = input("Date of transaction (mm-dd-yyyy): ")
        try:
            os.system("cls")
            with open(f"{name.split()[-1]}_{date}_Receipt.txt", "r", encoding='utf-8') as file:
                print(file.read())
                break
        except FileNotFoundError:
            print("Receipt not found!")
            time.sleep(2)
            continue
    while True:
        choice = input("Would you like to view another receipt? (Y/N) ")
        if choice.upper() == "Y":
            view_receipt()
            break
        elif choice.upper() == "N":
            main_menu()
            break
        else:
            print("Invalid Input!")
            time.sleep(2)

def view_transactions():
    """Asks the user if they want to look for a specific transaction or all transactions."""
    while True:
        os.system("cls")
        print("Would you like to view a specific transaction or all transactions?")
        print("1. Specific Transaction")
        print("2. All Transactions")
        choice = input("Enter your choice: ")
        if choice == "1":
            specific_transaction()
            break
        elif choice == "2":
            all_transactions()
            break
        else:
            print("Invalid Input!")
            time.sleep(2)

def specific_transaction():
    """Displays the transaction of the user based on their name or date of transaction."""
    while True:
        os.system("cls")
        print("Would you like to search for a transaction based on name or date?")
        print("1. Name")
        print("2. Date")
        choice = input("Enter your choice: ")
        if choice == "1":
            search_name()
            break
        elif choice == "2":
            search_date()
            break
        else:
            print("Invalid Input!")
            time.sleep(2)

def search_name():
    """Displays the transaction of the user based on their name using regex."""
    while True:
        os.system("cls")
        print("Please enter your name.")
        name = input("Name: ")
        try:
            os.system("cls")
            with open("Transactions.csv", "r") as file:
                for line in file:
                    if re.search(name, line, re.IGNORECASE):
                        name, contact_number, email, address, van_type, days, price, date = line.split(",")
                        print(f"Name: {name}\nContact Number: {contact_number}\nEmail: {email}\nAddress: {address}\nVan Type: {van_type}\nDays: {days}\nPrice: {price}\nRent Date: {date}\n")
                break
        except FileNotFoundError:
            print("Receipt not found!")
            time.sleep(2)
            continue
    while True:
        choice = input("Would you like to view another receipt? (Y/N) ")
        if choice.upper() == "Y":
            specific_transaction()
            break
        elif choice.upper() == "N":
            main_menu()
            break
        else:
            print("Invalid Input!")
            time.sleep(2)

def search_date():
    """Displays the transaction of the user based on the date of transaction using regex."""
    while True:
        os.system("cls")
        print("Please enter the date of your transaction in 'mm/dd/yyy' format.")
        date = input("Date: ")
        try:
            with open("Transactions.csv", "r") as file:
                print("Name, Contact Number, Email, Address, Van Type, Days, Price, Rent Date\n")
                for line in file:
                    if re.search(date, line):
                        print(line)
                break
        except FileNotFoundError:
            print("Receipt not found!")
            time.sleep(2)
            continue
    while True:
        choice = input("Would you like to view another receipt? (Y/N) ")
        if choice.upper() == "Y":
            specific_transaction()
            break
        elif choice.upper() == "N":
            main_menu()
            break
        else:
            print("Invalid Input!")
            time.sleep(2)

def all_transactions():
    """Displays all the transactions of the user."""
    while True:
        os.system("cls")
        try:
            print("Name, Contact Number, Email, Address, Van Type, Days, Price, Rent Date\n")
            with open("Transactions.csv", "r") as file:
                for line in file:
                    print(line)
                break
        except FileNotFoundError:
            print("Receipt not found!")
            time.sleep(2)
            continue
    while True:
        choice = input("Would you like to view another receipt? (Y/N) ")
        if choice.upper() == "Y":
            all_transactions()
            break
        elif choice.upper() == "N":
            main_menu()
            break
        else:
            print("Invalid Input!")
            time.sleep(2)




if __name__ == "__main__":
    main_menu()

        