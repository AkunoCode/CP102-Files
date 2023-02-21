import datetime

class VanRental:
    def __init__(self, renter_contact, renter_name, renter_address, rented_at):
        self.renter_contact = renter_contact
        self.renter_name = renter_name
        self.renter_address = renter_address
        self.rented_at = rented_at
        self.returned_at = None
        self.paid = False
    
    def calculate_price(self):
        if not self.returned_at: # If hindi pa sinasauli, wala pang babayadan
            return None
        time_difference = (self.returned_at - self.rented_at).total_seconds() / 3600 # Calculate kung ilang oras inarkila
        price = 200 * time_difference # Calculate yung payment per hour
        return price
    
    def return_van(self):
        self.returned_at = datetime.datetime.now() # Iset para isauli yung van
    
    def get_renter_contact(self):
        return self.renter_contact

    def get_renter_name(self):
        return self.renter_name

    def get_renter_address(self):
        return self.renter_address

    def get_rented_at(self):
        return self.rented_at

    def get_returned_at(self):
        return self.returned_at
    
    def get_rental_info(self):
        rental_info = {
            'renter_contact': self.renter_contact,
            'renter_name': self.renter_name,
            'renter_address': self.renter_address,
            'rented_at': self.rented_at,
            'returned_at': self.returned_at,
            'paid': self.paid
        }
        return rental_info


# EXAMPLE
def rentVan():
    contact = input("Enter the Renter's Contact Information: ")
    name = input("Enter the Renter's Name: ")
    address = input("Enter the Renter's Address: ")
    year, month, day = input("Enter the year, month, and day of rent. (YYYY,MM,DD): ").split()
    hour, minute = input("Enter hour and minute of start renting. (HH,MM): ").split()

    rental = VanRental(contact, name, address, datetime.datetime(int(year), int(month), int(day), int(hour), int(minute)))

    return rental

def main():
    rented_vans = []
    print("What would you like to do?: ")
    print("[1] Rent")
    print("[2] Return Van")
    print("[3] Exit")
    choice = input("Type the number of action chosen: ")
    if choice == 1:
        rent = rentVan()
        rented_vans.append()


if __name__ == "__main__":
    main()