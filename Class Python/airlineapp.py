class AirlineApp:
    def __init__(self):
        #Initialize flights list and bookings
        self.flights = []
        self.bookings = []
        #adding method - add new flight

    def add_flight(self, number, destination, flight):
        self.flights.append({'number': number, 'destination': destination, 'flight': flight, 'seats': 100 })

        #viewing method -> show all flights
    def view_flights(self):
        for f in self.flights:
            print(f"Flights {f['number']} to {f['destination']} - (Seats: {f['seats']})")

        #booking method - book a flight
    def book(s, num, name):
        for f in s.flights:
            if f["number"] == num and f["seats"] > 0:
                f["seats"] -= 1
                s.bookings.append({"name": name, "flight": num})
                print(f"{name} booked on {num}")
                return
        print("Booking failed.")
    #viewing method -> show bookings
    def view_booking(self):
        for b in self.bookings:
            print(f"{b['name']} booked on {b['flight']}")
    #main menu

app = AirlineApp()
while True:
    print("\n=== Airline Menu ===")
    print("1. Add Flight")
    print("2. View Flights")
    print("3. Book Flight")
    print("4. View Bookings")
    print("5. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        num = input("Flight Number: ")
        dest = input("Destination: ")
        flight = input("Flight Name: ")
        app.add_flight(num, dest, flight)
    elif choice == '2':
        app.view_flights()
    elif choice == '3':
        num = input("Flight Number to book: ")
        name = input("Passenger Name: ")
        app.book(num, name)
    elif choice == '4':
        app.view_booking()
    elif choice == '5':
        break
    else:
        print("Invalid choice.")


    

