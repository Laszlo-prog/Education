#create ticket booking application usin python
class Ticket:
    def __init__(self ):
        self.tickets = []
        self.booked_seats = set()

    def book_ticket(self):
        name = input("Enter your name: ")
        seat = input("Enter seat number: ")

        if seat in self.booked_seats:
            print(f"Seat {seat} is already booked")

        else:
            ticket = Ticket(name, seat)
            self.tickets.append(ticket)
            self.booked_seats.add(seat)
            print(f"Ticket booked successfully for {name} at seat {seat}")

    def view_tickets(self):
        if not self.tickets:
            print("No tickets booked yet.")
        else: 
            print("\nBooked Tickets:")
            for ticket in self.tickets:
                print(f"Name: {ticket.name}, Seat: {ticket.seat}")

#Cancel a booked ticket
    def cancel_ticket(self):
        seat = input("Enter seat number to cancel: ")

        for ticket in self.tickets:
            if ticket.seat == seat:
                self.tickets.remove(ticket)
                self.booked_seats.remove(seat)
                print(f"Ticket for seat {seat} cancelled successfully.")
                return
                    
        print(f"No ticket found for seat {seat}.")

    def menu(self):
        while True:
            print("\nTicket Booking System")
            print("1 Book Ticket")
            print("2 View Tickets")
            print("3 Cancel Ticket")
            print("4 Exit")

            choice = input("Choose an option (1-4): ")
            if choice == '1':
                self.book_ticket()
            elif choice == '2':
                self.view_tickets()
            elif choice == '3':
                self.cancel_ticket()
            elif choice == '4':
                print("Exiting the Ticket Booking System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = Ticket()
    app.menu()
    

