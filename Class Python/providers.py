class Provider:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    #Show provider info

    def show_info(self):
        return f"Provider Name: {self.name}, Rating: {self.rating}/5"

#Service class

class Service:
    def __init__(self, name, price, provider):
        self.name = name
        self.price = price
        self.provider = provider
    
    #Show service with provider
    def show(self):
        return f"Service: {self.name}, Price: ${self.price:.2f}"
        #print(f"Provided by: {self.provider.show_info()}")

#app class

class ServiceApp:
    def __init__(self):
        self.services = [ 
            Service("Web Design", 500.0, Provider("Alice", 4.5)),
            Service("SEO Optimization", 300.0, Provider("Bob", 4.0)),
            Service("Content Writing", 150.0, Provider("Charlie", 4.8))
        ]

        self.cart = []

#Show services
    def show_services(self):
        for i, s in enumerate(self.services):
            print(f"{i + 1}. {s.show()} - Provided by: {s.provider.show_info()}") 

    def add_to_cart(self, idx):
        self.cart.append(self.services[idx])
        print("Add to cart")

    def show_cart(self):
        if not self.cart: print("Cart is empty"); return
        for s in self.cart: s.show()

    def checkout(self):
        total = sum(s.price for s in self.cart) 
        print(f"Total = ${total:.2f}")


    #Run the app
app = ServiceApp()
while True:
    print("\nAvailable Services:")
    app.show_services()
    print("\nOptions:")
    print("1. Add to Cart")
    print("2. View Cart")
    print("3. Checkout")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        idx = int(input("Enter service number to add to cart: ")) - 1
        if 0 <= idx < len(app.services):
            app.add_to_cart(idx)
        else:
            print("Invalid service number.")
    elif choice == '2':
        print("\nYour Cart:")
        app.show_cart()
    elif choice == '3':
        app.checkout()
    elif choice == '4':
        print("Exiting Service App.")
        break
    else:
        print("Invalid choice. Please try again.")


