import matplotlib.pyplot as plt

class Visualization:


    def plot_price(self, prices):

        plt.figure(figsize=(10,4))

        plt.plot(prices)

        plt.title("Market Price")

        plt.xlabel("Step")

        plt.ylabel("Price")

        plt.grid()

        plt.show()



    def plot_pnl(self, pnl_history):

        plt.figure(figsize=(10,4))

        plt.plot(pnl_history)

        plt.title("PnL Curve")

        plt.xlabel("Step")

        plt.ylabel("PnL")

        plt.grid()

        plt.show()



    def plot_inventory(self, inventory_history):

        plt.figure(figsize=(10,4))

        plt.plot(inventory_history)

        plt.title("Inventory")

        plt.xlabel("Step")

        plt.ylabel("Position")

        plt.grid()

        plt.show()