import random


class MarketSimulator:

    def __init__(self, initial_price=100):
        self.price = initial_price


    def update_price(self):

        movement = random.gauss(0, 0.1)

        self.price += movement

        return self.price


    def next_price(self):

        movement = random.gauss(0,0.1)

        return self.price + movement