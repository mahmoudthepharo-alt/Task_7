class Passenger:
    def __init__(self, name):
        self.name = name


class Flight:
    def __init__(self):
        self.passengers = []

    def add_passenger(self, passenger_obj):
        self.passengers.append(passenger_obj)
        print(f"{passenger_obj.name} added to the flight.")


flight = Flight()

while True:
    print("\n 1- Add Passenger \n 2- Exit ")

    choice = int(input("Choose an option: "))

    if choice == 1:
        name = input("Enter passenger name: ")
        passenger = Passenger(name)
        flight.add_passenger(passenger)
        print("\nPassenger List:")
        for passenger in flight.passengers:
            print("-", passenger.name)

    elif choice == 2:
        print("Exit")
        break

    else:
        print("Invalid option, try again.")