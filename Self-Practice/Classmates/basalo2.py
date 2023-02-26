import os
import time
import datetime


class VanRental:
    def __init__(self, name, age, password, email, sex, phone, address, bdate):
        self.__name = name
        self.__age = age
        self.__password = password
        self.__email = email
        self.__sex = sex
        self.__phone = phone
        self.__address = address
        self.__bdate = bdate
        self.__rent_at = None
        self.__returned_at = None

    def getPersonDetails(self):
        details = {
            "name": self.__name,
            "age": self.__age,
            "password": self.__password,
            "email": self.__email,
            "sex": self.__sex,
            "phone": self.__phone,
            "address": self.__address,
            "bdate": self.__bdate
        }
        return details

    def createReceipt(self):
        with open('Receipt.txt', 'w') as receipt:
            receipt.write()


Accounts = []

rent_at = input("Enter rent date (MM/DD/YYYY): ")
rent_at = datetime.datetime.strptime(rent_at, "%m/%d/%Y")


def saveAccount(account):
    pass


def createAccount():
    os.system('cls')
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    password = input("Enter a password: ")
    email = input("Enter your email address: ")
    sex = input("Enter your gender: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")
    bdate = input("Enter your birthdate (DD/MM/YYYY): ")

    van_rental = VanRental(name, age, password, email,
                           sex, phone, address, bdate)
    return van_rental


def loginAccount():
    while True:
        os.system('cls')
        email = input("Enter your account email: ")
        for account in Accounts:
            if account.getPersonDetails()["email"] == email:
                password = input("Enter your account password: ")
                if account.getPersonDetails()["password"] == password:
                    print("Log-in Successful")
                    rentalScreen(account)
                    break
        print("No Email Match Found")
        time.sleep(0.5)


def introScreen():
    while True:
        os.system('cls')
        print("\nWelcome to Terownie's Van Rental\n")
        print("[1] Log-in")
        print("[2] Register")
        print("[3] Exit")
        choice = input("\nWhich action would you like to perform?: ")
        if choice == "1":
            loginAccount()
        elif choice == "2":
            new_acc = createAccount()
            Accounts.append(new_acc)
        elif choice == "3":
            os.system('cls')
            print("Thank you for using Terownie's Service!")
            time.sleep(3)
            exit()
        else:
            print("Invalid Choice")


def rentalScreen(account):
    while True:
        os.system('cls')
        print(
            f"Welcome {account.getPersonDetails()['name']} How can Terownie serve you?")
        print("[1] Book a Van")
        print("[2] Sign-out")
        choice = input("Select an action to perform: ")
        if choice == "1":
            ""
        elif choice == "2":
            return


def rentVan():
    ""


if __name__ == '__main__':
    introScreen()
