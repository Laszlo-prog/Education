import time
print("=========================")
print("==My Stock===============")
print("=========================")

my_stock = {"Marca": 'Audi', "Model" :'A5', "An": 2017}

def add_stock():
    print("Add new stock:")
    item = input("Item:")
    num_items = int(input("Number of items:"))
    my_stock[item] = num_items
    print("Upload...")
    time.sleep(1)
    print("Stock upload:", my_stock)

add_stock()