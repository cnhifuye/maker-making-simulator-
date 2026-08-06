import random


class OrderFlow:


    def __init__(self, informed_probability=0.2):

        self.informed_probability = informed_probability



    def generate_order(self, current_price, future_price):


        trader_type = random.random()



        # informed trader

        if trader_type < self.informed_probability:


            if future_price > current_price:

                return "BUY", "INFORMED"


            else:

                return "SELL", "INFORMED"



        # noise trader

        else:


            if random.random() < 0.5:

                return "BUY", "NOISE"

            else:

                return "SELL", "NOISE"