class StockMarketApp:
    def __init__(self):
        self.price = {"AAPl": 150.0, "GOOG": 2800.0, "AMZN": 3400.0 }
        self.portfolio = Portfolio()

        def menu(self):
            print("\n======Mini stock market app======" )
            print("1. View prices")
            print("2. Buy shares")
            print("3. Sell shares")
            print("4. View portfolio")
            print("5. Exit")

        def run (self):
            while True:
                self.menu()
                choice = input("Enter your choice: ")
                if choice == '1':
                    self.view_prices()
                elif choice == '2':
                    self.buy_shares()
                elif choice == '3':
                    self.sell_shares()
                elif choice == '4':
                    self.view_portfolio()
                elif choice == '5':
                    print("Exiting the app.")
                    break
                else:
                    print("Invalid choice. Please try again.")

                def  show_prices(self):
                    for sym, price in self.price.items():
                        print(f"{sym}: ${price}")

                def buy_flow(self):
                    symbol = input("Enter stock symbol to buy: ").upper()
                    qty = int(input("Enter quantity to buy: "))
                    if symbol in self.price and qty > 0 :
                        self.portfolio.buy(symbol, qty, self.price[symbol])
                    else:
                        print("Invalid stock symbol or quantity.")  
                def sell_flow(self):
                    symbol = input("Enter stock symbol to sell: ").upper()
                    qty = int(input("Enter quantity to sell: "))
                    if self.portfolio.sell(symbol, qty, self.price.get(symbol, 0)):

                        print(f"Sold {qty} shares of {symbol}.")

                    else:
                        print("Invalid stock symbol or insufficient shares to sell.")   

class Portfolio:
    def __init__(self):
       self.cash = 10000.0  # Starting cash
       self.shares = {}

    def buy(self, symbol, qty, price):
        cost = qty * price
        if self.cash >= cost:
            self.cash -= cost
            self.holdings[symbol] = self.holdings.get(symbol, 0) + qty
            print(f"Bought {qty} shares of {symbol} at ${price} each.")

        else:
            print("Insufficient cash to buy shares.")   


    def sell(self, symbol, qty, price):
        if self.holdings.get(symbol, 0) >= qty:
            self.holdings[symbol] -= qty
            self.cash += qty * price
            print(f"Sold {qty} shares of {symbol} at ${price} each.")
            return True
        return False

    def show(self):
        print("\n=== Portfolio ===")
        
        for symbol, qty in self.holdings.items():
            print(f"{symbol}: {qty} shares")

        print(f"Cash: ${self.cash:.2f}")

    def min():
        StockMarketApp().run()

if __name__ == "__main__":
    min()

        
