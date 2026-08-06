from order import Order
class OrderBook:


    def __init__(self):

        self.bids = []

        self.asks = []



    def add_order(
    self,
    owner,
    side,
    price,
    quantity,
    timestamp
    ):

        order = Order(
        owner,
        side,
        price,
        quantity,
        timestamp
    )

        if side == "BUY":

            self.bids.append(order)

        else:

            self.asks.append(order)

    def sort_book(self):

        self.bids.sort(
        key=lambda x:x.price,
        reverse=True
        )

        self.asks.sort(
        key=lambda x:x.price
        )

    def best_bid(self):

        if len(self.bids)==0:

            return None

        return self.bids[0].price



    def best_ask(self):

        if len(self.asks)==0:

            return None

        return self.asks[0].price