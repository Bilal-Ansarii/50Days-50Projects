class Train:
    def _init_(self, name, number, from_station, to_station, ac1stclass, ac2ndclass, ac3rdclass, sleeper, general):
        self.name = name
        self.number = number
        self.from_station = from_station
        self.to_station = to_station
        self.ac1stclass = ac1stclass
        self.ac2ndclass = ac2ndclass
        self.ac3rdclass = ac3rdclass
        self.sleeper = sleeper
        self.general = general


class Ticket:
    def _init_(self, name, age, train, class_type, num_tickets, from_station, to_station):
        self.name = name
        self.age = age
        self.train = train
        self.class_type = class_type
        self.num_tickets = num_tickets
        self.from_station = from_station
        self.to_station = to_station

trains = []
reserved_tickets = []

def add_train_manually():
    print("*** ONLY FOR RAILWAY TICKET RESERVATION DEPARTMENT'S EMPLOYEES ****")
    name = input("Enter Train Name: ")
    number = input("Enter Train Number: ")
    from_station = input("departure_venue: ")
    to_station = input("departure_venue: ")
    ac1stclass = int(input("Enter availablity of AC 1st class seats: "))
    ac2ndclass = int(input("Enter availablity of AC 2nd class seats: "))
    ac3rdclass = int(input("Enter availablity of AC 3rd class seats: "))
    sleeper = int(input("Enter availablity of sleeper class seats: "))
    general = int(input("Enter availablity of sleeper class seats: "))

    train = Train(name, number, from_station, to_station, ac1stclass, ac2ndclass, ac3rdclass, sleeper, general)
    trains.append(train)
    print("Successfully added train to list of available train !")

def delete_train_manually():
    if not trains:
        print("No trains available are available at this time.")
    else:
        display_trains()
        train_number = input("Enter Train Number to delete from list: ")
        train = next((t for t in trains if t.number == train_number), None)
        if train:
            trains.remove(train)
            print(f"Train {train.name} (Number: {train.number}) deleted successfully.")
        else:
            print("Train not found.")

def display_trains():
    if not trains:
        print("No trains are available.")
    else:
        print("Available Trains:")
        for train in trains:
            print("******************")
            print(f"Train Name: {train.name}, Train Number: {train.number}")
            print(f"From: {train.from_station}, To Number: {train.to_station}")
            print("******************")
            print(f"AC 1st Class: {train.ac1stclass}, AC 2nd Class: {train.ac2ndclass}")
            print(f"AC 3rd Class: {train.ac3rdclass}, Sleeper Class: {train.sleeper}")
            print("=" * 30)
        print("******************")

def reserve_ticket():
    display_trains()
    if not trains:
        print("No trains are available for reservations.")
    else:
        train_number = input("Enter Train Number for Reservation: ")
        train = next((t for t in trains if t.number == train_number), None)
        departure_station = input("Enter Departure Station: ")
        destination_station = input("Enter Destination Station: ")
        if train:
            print(f"Train Name: {train.name}")
            class_type = input("Enter Class (AC1/AC2/AC3/Sleeper/General): ")
            num_tickets = int(input("Enter Number of Tickets: "))
            for i in range(num_tickets):
                passenger_name = input(f"Enter Passenger {i+1} Name: ")
                passenger_age = input(f"Enter Passenger {i+1} Age: ")
                ticket = Ticket(passenger_name, passenger_age, train, class_type, 1, departure_station, destination_station)  # Pass the train object
                reserved_tickets.append(ticket)
                if class_type == 'AC1' and train.ac1stclass >= 1:
                    train.ac1stclass -= 1
                    print(f"Ticket reserved for AC1 successfully for Passenger {i+1}!")
                elif class_type == 'AC2' and train.ac2ndclass >= 1:
                    train.ac2ndclass -= 1
                    print(f"Ticket reserved for AC2 successfully for Passenger {i+1}!")
                elif class_type == 'AC3' and train.ac3rdclass >= 1:
                    train.ac3rdclass -= 1
                    print(f"Ticket reserved for AC3 successfully for Passenger {i+1}!")
                elif class_type == 'Sleeper' and train.sleeper >= 1:
                    train.sleeper -= 1
                    print(f"Ticket reserved for Sleeper successfully for Passenger {i+1}!")
                elif class_type == 'General' and train.general >= 1:
                    train.general -= 1
                    print(f"Ticket reserved for General successfully for Passenger {i+1}!")
                else:
                    print("Invalid class or insufficient seats.")
        else:
            print("Train not found.")



def display_reserved_tickets():
    if not reserved_tickets:
        print("No tickets have been reserved.")
    else:
        print("Reserved Tickets:")
        print("******************")
        for ticket in reserved_tickets:
            print(f"Passenger Name: {ticket.name}  |  Passenger Age: {ticket.age}")
            print(f"From : {ticket.from_station}  |  To : {ticket.to_station}")
            print(f"Train Name: {ticket.train.name}  |  Train Number: {ticket.train.number}")
            print(f"Class Type: {ticket.class_type}  |  Number of Tickets: {ticket.num_tickets}")
            print("=" * 30)
  

def main():
    while True:
        print("\nRailway Ticket Reservation System")
        print("1. Display Available Trains")
        print("2. Reserve Ticket")
        print("3. Display Reserved Tickets")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_trains()
        elif choice == '2':
            reserve_ticket()
        elif choice == '3':
            display_reserved_tickets()
        elif choice == '4':
            print("Exiting the system.")
            break
        elif choice == '5':
            add_train_manually()
        elif choice == '6':
            delete_train_manually()    
        else:
            print("Invalid choice. Please try again.")

if __name__== "_main_":
    main()