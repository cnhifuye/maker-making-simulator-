class MarketMaker:


    def __init__(self, spread=0.1):

        self.spread = spread

        self.cash = 10000

        self.inventory = 0



    def make_quote(self, price):


        inventory_skew = self.inventory * 0.01


        bid = (
            price
            - self.spread / 2
            - inventory_skew
        )


        ask = (
            price
            + self.spread / 2
            - inventory_skew
        )


        return bid, ask



    def place_orders(self, order_book, price,step):


        bid, ask = self.make_quote(price)

        order_book.add_order(
        "market_maker",
        "BUY",
        bid,
        1,
        step
        )


        order_book.add_order(
        "market_maker",
        "BUY",
        bid,
        1,
        step
        )
    
    def execute_trade(self, side, price, quantity):


        if side == "BUY":

            self.inventory += quantity

            self.cash -= price * quantity


        elif side == "SELL":

            self.inventory -= quantity

            self.cash += price * quantity