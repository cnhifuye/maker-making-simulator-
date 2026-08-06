import numpy as np


class Performance:


    def __init__(self):

        self.pnl_history = []

        self.trade_count = 0



    def record(self, pnl, filled):


        self.pnl_history.append(pnl)


        if filled:

            self.trade_count += 1



    def total_return(self):

        return (
            self.pnl_history[-1]
            -
            self.pnl_history[0]
        )



    def sharpe_ratio(self):


        returns = np.diff(
            self.pnl_history
        )


        if np.std(returns) == 0:

            return 0


        return (
            np.mean(returns)
            /
            np.std(returns)
            *
            np.sqrt(252)
        )



    def max_drawdown(self):


        peak = self.pnl_history[0]

        max_dd = 0


        for pnl in self.pnl_history:


            if pnl > peak:

                peak = pnl


            drawdown = peak - pnl


            if drawdown > max_dd:

                max_dd = drawdown


        return max_dd