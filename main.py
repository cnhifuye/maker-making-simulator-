from market_simulator import MarketSimulator
from market_maker import MarketMaker
from order_flow import OrderFlow
from performance import Performance
from execution import ExecutionEngine
from order_book import OrderBook
from portfolio import Portfolio
from visualization import Visualization

market = MarketSimulator()

maker = MarketMaker()

flow = OrderFlow()

performance = Performance()

execution = ExecutionEngine()

book = OrderBook()

portfolio = Portfolio()

prices = []

pnl_history = []

inventory_history = []


for step in range(20):

    future_price = market.next_price()

    price = market.update_price()


    bid, ask = maker.make_quote(price)


    order, trader_type = flow.generate_order(
        price,
        future_price
    )


    if order == "BUY":

        quote_price = ask

    else:

        quote_price = bid


    filled = execution.execute(
        order,
        price,
        quote_price
    )


    if filled:


        if order == "BUY":

        # trader buys
        # market maker sells

            portfolio.process_trade(
            "SELL",
                quote_price,
            1
        )


        else:

        # trader sells
        # market maker buys

            portfolio.process_trade(
            "BUY",
            quote_price,
            1
        )

    pnl = portfolio.value(price)

    prices.append(price)

    pnl_history.append(pnl)

    inventory_history.append(
    portfolio.inventory
    )

    performance.record(
    pnl,
    filled
    )
    print(
        f"""
Step {step}
Price: {price:.2f}
Order: {order}
Filled: {filled}
Trader: {trader_type}
Inventory: {portfolio.inventory}
Cash: {portfolio.cash}
PnL: {pnl:.2f}
"""
    )

print(
    "\n===== Performance ====="
)


print(
    "Trades:",
    performance.trade_count
)


print(
    "Total Return:",
    performance.total_return()
)


print(
    "Sharpe:",
    performance.sharpe_ratio()
)


print(
    "Max Drawdown:",
    performance.max_drawdown()
)

visualizer = Visualization()


visualizer.plot_price(
    prices
)


visualizer.plot_pnl(
    pnl_history
)


visualizer.plot_inventory(
    inventory_history
)