class RestaurantApp:
    def __init__(self):
        self.menu = {
            "Pizza" : 350,
            "Burger" : 250,
            "Pasta" : 300,
            "Salad" : 150,
            "Fries" :100,
            "Drink" : 50,
            "Dessert" : 200,
            "Ice Cream" : 80,
            "Juice" : 120,
            "Shake" : 180
            
            

        }
        self.orders = { }

#View menu method
    def show_menu(self):
        print("Menu:")
        for item, price in self.menu.items():
            print(f"{item}: ${price}")

    def take_order(self):
        self.show_menu()
        print("\nEnter the name of the item to order (or 'done' to finish): ")

        while True:
            item = input("Item:").strip().title()
            if item.lower() == 'done':
                break
            elif item in self.menu:
                quantity = int(input(f"Enter quantity for {item}: "))
                if item in self.orders:
                    self.orders[item] += quantity
                else:
                    self.orders[item] = quantity
                print(f"Added {quantity} x {item} to your order.")
            else:
                print("Item not on the menu. Please try again.")
                break
                

    def view_bill(self):
        if not self.orders:
            print("No items ordered yet.")
            return

        print("\nYour Order:")
        total = 0
        for item, quantity in self.orders.items():
            price = self.menu[item]
            item_total = price * quantity
            total += item_total
            print(f"{item} x {quantity} = ${item_total}")

        print(f"Total Bill: ${total}")

    def run(self):
        
        while True:
            print("\nWelcome to the Restaurant App!")
            print("1. View Menu")
            print("2. Take Order")
            print("3. View Bill")
            print("4. Exit")

            choice = input("Choose an option (1-4): ")

            if choice == '1':
                self.show_menu()
            elif choice == '2':
                self.take_order()
            elif choice == '3':
                self.view_bill()
            elif choice == '4':
                print("Thank you for using the Restaurant App. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

                

if __name__ == "__main__":
    app = RestaurantApp()
    app.run()
