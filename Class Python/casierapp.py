import datetime

class Item:
    def __init__(self, item_id, name, quantity, price):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.quantity * self.price
    
class Casier:
        def __init__(self):
            self.cart = []
            self.next_id = 1
            self.discount = 0

    #add item to cart
        def add_item(self, name, price, quantity):
            item = Item(self.next_id, name, quantity, price)
            self.cart.append(item)
            self.next_id += 1
            print(f"Added {quantity} of {name} to cart.")

    #view cart items
        def view_cart(self):
            if not self.cart:
                print("Cart is empty.")
                return
            print("\nCart Items:")
            for item in self.cart:
                print(f"ID: {item.item_id}, Name: {item.name}, Quantity: {item.quantity}, Price: ${item.price}, Total: ${item.total()}")
            print(f"Subtotal: ${self.calculate_subtotal()}")
            if self.discount > 0:
                print(f"Discount: {self.discount}%")
                print(f"Total after discount: ${self.calculate_total()}")
            else:
                print(f"Total: ${self.calculate_total()}")
    #remove item by ID

def remove_item(self, item_id):
        for item in self.cart:
            if item.item_id == item_id:
                self.cart.remove(item)
                print(f"Removed {item.name} from cart.")
                return
        print(f"No item found with ID {item_id}.")
    #apply discount

def apply_discount(self, percentage):
        self.discount = percentage
        print(f"Applied {percentage}% discount to the cart.")
    
    #check and print bill
def checkout(self):
        if not self.cart:
            print("Cart is empty. Cannot checkout.")
            return
        
        subtotal = sum(item.total() for item in self.cart)
        discount_amount = (self.discount / 100) * subtotal
        total = subtotal - discount_amount
        print("\n----- Bill -----")

        print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        for item in self.cart:
            print(f"{item.name} (x{item.quantity}): ${item.total()}")
        print(f"Subtotal: ${subtotal}")
        print(f"Discount: {self.discount}% (-${discount_amount})")
        print(f"Total: ${total}")
        print("----------------")
        self.cart.clear()
        self.discount = 0

#main program loop
def menu(self):

        while True:
            print("\nCasier System")
            print("1. Add Item")
            print("2. View Cart")
            print("3. Remove Item")
            print("4. Apply Discount")
            print("5. Checkout")
            print("6. Exit")

            choice = input("Choose an option (1-6): ")
            if choice == '1':
                name = input("Enter item name: ")
                price = float(input("Enter item price: "))
                quantity = int(input("Enter item quantity: "))
                self.add_item(name, price, quantity)
            elif choice == '2':
                self.view_cart()
            elif choice == '3':
                item_id = int(input("Enter item ID to remove: "))
                self.remove_item(item_id)
            elif choice == '4':
                percentage = float(input("Enter discount percentage: "))
                self.apply_discount(percentage)
            elif choice == '5':
                self.checkout()
            elif choice == '6':
                print("Exiting the Casier System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

def calculate_subtotal(self):
        return sum(item.total() for item in self.cart)

def calculate_total(self):
        subtotal = self.calculate_subtotal()
        discount_amount = (self.discount / 100) * subtotal
        return subtotal - discount_amount

if __name__ == "__main__":
    app = Item()
    app.menu()
