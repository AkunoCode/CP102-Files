import re

class CoffeShop:
    def __init__(self, CoffeeType, Size):
        self.CoffeeType = CoffeeType
        self.Size = Size

    def Price(self):
        if self.Size == "Small":
            price = 170
        elif self.Size == "Medium":
            price = 200
        elif self.Size == "Large":
            price = 230
        else:
            price = 0
        return price
    
    def set_type(self, CoffeeType):
        self.CoffeeType = CoffeeType

    def calculate_price(self):
        if self.Size == "Small":
            return 170
        elif self.Size == "Medium":
            return 200
        elif self.Size == "Large":
            return 230
        else:
            return 0
    
    def get_type(self):
        if self.CoffeeType == "Cappuccino Espresso":
            return "Cappuccino Espresso"
        elif self.CoffeeType == "Latte":
            return "Latte"
        elif self.CoffeeType == "Mocha Macchiato":
            return "Mocha Macchiato"
        elif self.CoffeeType == "Cortado":
            return "Cortado"
        else:
            return "Invalid Choice."
    
    def get_total_price(self):
        total_price = 0
        for order in orders:
            total_price += order['price']
        return total_price
            
if __name__ == "_main_":
    print("\n")
    print("="*30)
    print("Main Menu")
    print("="*30)
    print("1. Coffee Type and Coffee Size")
    print("2. View your orders")
    print("3. Exit")

    orders = []
    while True:
        option = input("\nEnter the number you want to select: ")
        if option == "1":
            CoffeeType = input("\nEnter your coffee type: ") # The Coffee Types are  Cappuccino Espresso, Latte, Mocha Machiato, Cortado
            coffee = CoffeShop(CoffeeType, "")
            coffee.set_type(CoffeeType)
            Size = input("Enter your coffee size: ")
            coffee = CoffeShop(CoffeeType, Size)
            if Size in ["Small", "Medium", "Large"]:
                coffee = CoffeShop(CoffeeType, Size)
                order = {"type": coffee.get_type(), "size": Size, "price": coffee.Price()}
                orders.append(order)
                print("\nYour coffee is a", Size, CoffeeType, "and costs P", coffee.Price())
            else:
                print("Invalid choice!")
        elif option == "2":
            if orders:
                print("\nHere are the orders:")
                for order in orders:
                    print(f"{order['size']} {order['type']} - P{order['price']}")
                temp = CoffeShop("", "")
                print("Total price: P", temp.get_total_price())
            else:
                print("\nNo orders yet.")
        elif option == "3":
            print("\nThank you for visiting the coffee shop!")
            break
            exit()
        else:
            print("Invalid choice! Please enter 1 or 2.")