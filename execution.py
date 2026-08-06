import random


class ExecutionEngine:


    def __init__(self):

        pass



    def execute(self, order, market_price, quote_price):


        distance = abs(
            quote_price - market_price
        )


        probability = max(
            0,
            1 - distance * 5
        )


        random_number = random.random()


        return random_number < probability