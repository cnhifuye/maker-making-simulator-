class MatchingEngine:


    def match(self, order_book):


        trades = []


        while (
            order_book.bids
            and
            order_book.asks
            and
            order_book.best_bid()
            >=
            order_book.best_ask()
        ):


            bid_order = order_book.bids[0]

            ask_order = order_book.asks[0]


            trade_price = ask_order["price"]


            trade_quantity = min(
                bid_order.quantity,
                ask_order.quantity
            )


            trades.append(
            {
            "buyer":bid_order.owner,
            "seller":ask_order.owner,
            "price":trade_price,
            "quantity":trade_quantity
            }
            )

            bid_order["quantity"] -= trade_quantity

            ask_order["quantity"] -= trade_quantity



            if bid_order["quantity"] == 0:

                order_book.bids.pop(0)



            if ask_order["quantity"] == 0:

                order_book.asks.pop(0)



        return trades