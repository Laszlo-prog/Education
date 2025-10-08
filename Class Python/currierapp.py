class CurrierApp:

    def __init__(self):
        
        self.orders = []

    #Add a new order
    def add_order(self, n, a, c):
        self.orders.append({'name': n, 'address': a, 'contact': c, 'status': 'Pending'})
        print("Order added successfully.")

    #View all orders
    def view_orders(self):
        if not self.orders:
            print("No orders available.")
            return
        for i, o in enumerate(self.orders, 1):
            print(f"{i}. Name: {o['name']}, Address: {o['address']}, Contact: {o['contact']}, Status: {o['status']}")
    #Update status
    # 
    def update_status(self, i ):
        if 0 <= i < len(self.orders):

            self.orders[i]['status'] = "Delivered"

        else:
            print("Invalid order index.")

    def remove_order(self, i):
        if 0 <= i < len(self.orders):
            r = self.orders.pop(i)
            print(f"Removed order for {r['name']}.")
        else:
            print("Invalid order index.")

    #Show total earnings
    def total_earnings(self):
        total = len(self.orders) * 50  # Assuming each order earns $50
        print(f"Total Earnings: ${total}")

    def menu(self):
        while True:
            print("\nCurrier Service App")
            print("1. Add Order")
            print("2. View Orders")
            print("3. Update Order Status")
            print("4. Remove Order")
            print("5. Total Earnings")
            print("6. Exit")

            choice= input("Choose an option (1-6): ")
            if choice == '1':
                n = input("Enter customer name: ")
                a = input("Enter address: ")
                c = float(input("Enter contact number: "))
                self.add_order(n, a, c)
            elif choice == '2':
                self.view_orders()
            elif choice == '3':
                i = int(input("Enter order index to update status: ")) - 1
                self.update_status(i)
            elif choice == '4':
                i = int(input("Enter order index to remove: ")) - 1
                self.remove_order(i)
            elif choice == '5':
                self.total_earnings()
            elif choice == '6':
                print("Exiting the Currier Service App. Goodbye!")
                break

if __name__ == "__main__":
    app = CurrierApp()
    app.menu()
