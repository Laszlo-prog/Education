def stock():
    while True:
        stock = input("Enter the new stock:")
        if stock.isdigit():
            stock = int(stock)
            if stock > 0:
                continue
            else:
                print("Stock must be greater than 0:")
        else:
            print("Try again!!! ")
            break
    return ValueError


stock()