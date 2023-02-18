import re
import sys
import os

class Games:
    def __init__(self, name, genre, price):
        self.name = name
        self.genre = genre
        self.price = price
        
    def get_name(self):
        return self.name
    
    def get_genre(self):
        return self.genre
    
    def get_price(self):
        return self.price

gamelist = []
def create_game():
    print("Add details of your game. Enter 1 to cancel.")
    game_name = input("\nEnter game name: ")
    if game_name == "1":
        print("Cancelled operation.")
        return
    game_genre = input("Enter game genre: ")
    if game_genre == "1":
        print("Cancelled operation.")
        return
    game_price = input("Enter game price: ")
    if game_price == "1":
        print("Cancelled operation.")
        return
    save = input("Do you want to save the game [Y/N]?: ")
    if save.lower() == "y":
        saved = save_game(game_name, game_genre, game_price)
        gamelist.append(saved)

def save_game(game_name, game_genre, game_price):
    with open("Ian.txt", "a") as file:
        file.write(f"Game name: {game_name}\nGenre: {game_genre}\nPrice: {game_price}\n\n")
        print("\nGame added successfully!\n")
        return Games(game_name, game_genre, game_price)

def search_game():
     while True:
        matches = []
        where = input("\nEnter game name: ")
        for game in gamelist:
            if re.search(where, game.get_name(), re.IGNORECASE):
                matches.append(game)
        if len(matches) > 0:
            for game in matches:
                print(f"Game: {game.get_name()}")
                print(f"Genre: {game.get_genre()}")
                print(f"Price: {game.get_price()}\n")
        else:
            print("\nNo matches found.\n")
        again = input("Do you want to search again [Y/N]?: ")
        if again.lower() == "n":
            break

def read_file():
    namepat = r"(?<=Game name: ).+(?=\n)"
    genrepat = r"(?<=Genre: ).+(?=\n)"
    pricepat = r"(?<=Price: ).+(?=\n)"

    with open("Ian.txt", "r") as file:
        hand = file.read()
        game_name = re.findall(namepat, hand)
        game_genre = re.findall(genrepat, hand)
        game_price = re.findall(pricepat, hand)

    for x in range(len(game_name)):
        name = game_name[x]
        genre = game_genre[x]
        price = game_price[x]
        game = Games(name, genre, price)
        gamelist.append(game)

def main():
    os.system('cls')
    print("\nWelcome to the Game Library!")
    print("Here, you can add or search for a game you're looking for!\n")
    
    while True:
        print("\nWhat do you want to do?")
        print("[1] Add a game.")
        print("[2] Search for a game.")
        print("[3] Exit")
        name = input("\nEnter option: ")
        
        if name == "1":
            os.system('cls')
            create_game()
        elif name == "2":
            os.system('cls')
            search_game()                           
        elif name == "3":
            os.system('cls')
            print("\nThank you for using! Now exiting...")
            sys.exit()
        else:
            os.system('cls') 
            print("Please choose from the options. Try again.\n")
            continue

if __name__ == "__main__":
    read_file()
    main()
