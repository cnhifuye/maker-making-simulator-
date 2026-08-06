class Portfolio:


    def __init__(self, cash=10000):

        self.cash = cash

        self.inventory = 0



    def process_trade(self, side, price, quantity):

        if side == "BUY":

            self.inventory += quantity

            self.cash -= price * quantity


        elif side == "SELL":

            self.inventory -= quantity

            self.cash += price * quantity



    def value(self, market_price):

        return (
            self.cash
            +
            self.inventory * market_price
        )