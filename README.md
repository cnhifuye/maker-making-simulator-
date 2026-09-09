# Market Making Simulator with Limit Order Book

A Python-based market making simulator with a limit order book, matching engine, inventory management, and performance analytics.

# Overview

This project simulates a simplified electronic trading environment:

- Market makers provide bid/ask quotes
- Traders generate buy/sell orders
- Orders are matched through a limit order book
- Portfolio value and trading performance are tracked


# Architecture

Market Simulator
|
Market Maker
|
Order Book
|
Matching Engine
|
Portfolio
|
Performance Analysis



# Features

- Stochastic price simulation
  - Random price process for market dynamics

- Inventory-aware market making
  - Dynamic bid/ask quoting based on inventory exposure

- Limit Order Book
  - Bid/ask queues
  - Price priority matching

- Matching Engine
  - Order crossing
  - Trade execution

- Trader Simulation
  - Noise traders
  - Informed traders

- Performance Metrics
  - PnL
  - Sharpe ratio
  - Maximum drawdown
  - Trade count


# Results

The simulator produces:

- Price evolution
- PnL curve
- Inventory exposure


# Technologies

- Python
- NumPy
- Matplotlib


# Future Improvements

- Avellaneda-Stoikov optimal market making model
- More realistic order arrival process
- Queue position modeling
- Latency simulation

