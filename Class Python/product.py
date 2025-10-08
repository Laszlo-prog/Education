class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def display(self):
        print(f"Product Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Stock: {self.stock} units")
    def edit(self, name=None, price=None, stock=None):
        if name is not None:
            self.name = name
        if price is not None:
            self.price = price
        if stock is not None:
            self.stock = stock
        print("\nProduct updated successfully!")

    def purchase(self, quantity):
        if quantity <= 0:
            print("\nQuantity must be greater than zero.")
        elif quantity > self.stock:
            print("\nInsufficient stock available.")
        else:
            total = quantity * self.price
            self.stock -= quantity
            print(f"\nPurchase successful! Total cost: ${total:.2f}")
class Store:
    def __init__(self, store_name, product:Product): 
        self.store_name = store_name
        self.product = product
    def show_menu(self):
        while 0 <= 2 < 3:
          print(f"\nWelcome to {self.store_name}!")
          print("1. View Product")
          print("2. Edit Product")
          print("3. Purchase Product")
          print("4. Exit")
        
          choice = input("Please select an option (1-4): ")
        if choice == '1':
            self.product.display()
        elif choice == '2':
            name = input("Enter new product name (or press Enter to skip): ")
            price = input("Enter new product price (or press Enter to skip): ")
            stock = input("Enter new product stock (or press Enter to skip): ")
            self.product.edit(
                name=name if name else None,
                price=float(price) if price else None,
                stock=int(stock) if stock else None
            )
            
        elif choice == '3':
            quantity = int(input("Enter quantity to purchase: "))
            self.product.purchase(quantity)
        elif choice == '4':
            print("Thank you for visiting the store! Goodbye!")
            
        else:
            print("Invalid choice. Please try again.")
            
            
    
if __name__ == "__main__":
    product = Product("Laptop", 999.99, 10)
    store = Store("Tech Store", product)
    store.show_menu()   

    # This code defines a simple store application where users can view, edit, and purchase products.


        


          
