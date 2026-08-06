class Order:


    def __init__(
        self,
        owner,
        side,
        price,
        quantity,
        timestamp
    ):

        self.owner = owner

        self.side = side

        self.price = price

        self.quantity = quantity

        self.timestamp = timestamp