class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"
    

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, coffee):
        self.items.append(coffee)
        print(f"Added {coffee.name} to the order.")

    

    def total_price(self):
        return sum(item.price for item in self.items)

    def show_order(self):
        if not self.items:
            print("Your order is empty.")
            return
        print("\nYour order:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item} - ${item.price}")
        print(f"Total price: ${self.total_price()}\n")
    def checkout(self):
        if not self.items:
            print("Your order is empty. Please add items before checking out.")
            return
        print("Checking out...")
        self.show_order()
        confirm = input("Do you want to confirm your order? (yes/no): ").strip().lower()
        if confirm == 'yes':
            print("Order confirmed!")
        else:
            print("Order cancelled.")
            return
        print("Thank you for your order!")
        self.items.clear()
        # display menu and handle user input
def main():
    order = Order()
    menu = [
        Coffee("Espresso", 2.50),
        Coffee("Latte", 3.75),
        Coffee("Cappuccino", 4.00),
        Coffee("Americano", 2.00),
        Coffee("Mocha", 4.50),
        Coffee("Ciocolato", 3.25),
        Coffee("Milkshake", 3.70),
        Coffee("Tea", 1.50)
    ]

    while True:
        print("\nCoffee Menu:")
        for i, coffee in enumerate(menu, 1):
            print(f"{i}. {coffee}")
        
        choice = input("Select a coffee by number (or type 'checkout' to finish): ").strip().lower()
        
        if choice == 'checkout':
            order.checkout()
            break
        
        if choice.isdigit() and 1 <= int(choice) <= len(menu):
            order.add_item(menu[int(choice) - 1])
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
