import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# ------------------------------------
# PROJECT SETTINGS
# ------------------------------------
allowed_stocks = ["AAPL", "TSLA", "MSFT", "AMZN"]
start_date = "2018-01-01"
end_date = "2024-01-01"
days = 252
simulations = 1000
short_window = 10
long_window = 50
stop_loss_threshold = 0.8

# ------------------------------------
# USER INPUT FOR STOCK SELECTION
# ------------------------------------
print("Available stock options: AAPL, TSLA, MSFT, AMZN")
stock = input("Enter stock ticker symbol (press Enter for AAPL): ").strip().upper()

if stock == "":
    stock = "AAPL"

if stock not in allowed_stocks:
    print("Invalid stock ticker. Please choose only from: AAPL, TSLA, MSFT, AMZN")
    sys.exit()

# ------------------------------------
# DOWNLOAD AND PREPARE HISTORICAL DATA
# ------------------------------------
data = yf.download(stock, start=start_date, end=end_date)

if data.empty:
    print("No data found for the selected stock. Please run the program again.")
    sys.exit()

# Fix multi-index columns if needed
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)

# Calculate daily returns
data["Daily Return"] = data["Close"].pct_change()
data = data.dropna()

# Historical statistics
mean_return = data["Daily Return"].mean()
volatility = data["Daily Return"].std()
last_price = data["Close"].iloc[-1]

print(f"\nSelected Stock: {stock}")
print("Mean Daily Return:", mean_return)
print("Daily Volatility:", volatility)

# ------------------------------------
# MONTE CARLO SIMULATION
# ------------------------------------
simulation_results = np.zeros((days, simulations))

for sim in range(simulations):
    price_path = [last_price]

    for _ in range(days):
        random_return = np.random.normal(mean_return, volatility)
        next_price = price_path[-1] * (1 + random_return)
        price_path.append(next_price)

    simulation_results[:, sim] = price_path[1:]

# Plot Monte Carlo paths
plt.figure(figsize=(10, 6))
for sim in range(simulations):
    plt.plot(simulation_results[:, sim], linewidth=0.5)

plt.title(f"Monte Carlo Simulation of Future Stock Prices ({stock})")
plt.xlabel("Days")
plt.ylabel("Price")
plt.show()

# ------------------------------------
# FINAL PRICE ANALYSIS
# ------------------------------------
final_prices = simulation_results[-1, :]

mean_final_price = np.mean(final_prices)
median_final_price = np.median(final_prices)
max_price = np.max(final_prices)
min_price = np.min(final_prices)

print("\nSIMULATION RESULTS:")
print("Average Final Price:", mean_final_price)
print("Median Final Price:", median_final_price)
print("Best Case Price:", max_price)
print("Worst Case Price:", min_price)

plt.figure(figsize=(10, 5))
plt.hist(final_prices, bins=50)
plt.title(f"Distribution of Simulated Future Prices ({stock})")
plt.xlabel("Final Price After 252 Days")
plt.ylabel("Frequency")
plt.show()

# ------------------------------------
# BUY AND HOLD STRATEGY
# ------------------------------------
buy_and_hold_profits = final_prices - last_price

print("\nBUY AND HOLD STRATEGY RESULTS:")
print("Average Profit:", np.mean(buy_and_hold_profits))
print("Best Profit:", np.max(buy_and_hold_profits))
print("Worst Loss:", np.min(buy_and_hold_profits))

plt.figure(figsize=(10, 5))
plt.hist(buy_and_hold_profits, bins=50)
plt.title(f"Buy and Hold Profit Distribution ({stock})")
plt.xlabel("Profit After 252 Days")
plt.ylabel("Frequency")
plt.show()

# ------------------------------------
# MOVING AVERAGE STRATEGY
# ------------------------------------
ma_profits = []

for sim in range(simulations):
    prices = simulation_results[:, sim]
    position = 0
    buy_price = 0
    profit = 0

    for day in range(long_window, days):
        short_ma = np.mean(prices[day - short_window:day])
        long_ma = np.mean(prices[day - long_window:day])

        if short_ma > long_ma and position == 0:
            buy_price = prices[day]
            position = 1

        elif short_ma < long_ma and position == 1:
            profit += prices[day] - buy_price
            position = 0

    if position == 1:
        profit += prices[-1] - buy_price

    ma_profits.append(profit)

print("\nMOVING AVERAGE STRATEGY RESULTS:")
print("Average Profit:", np.mean(ma_profits))
print("Best Profit:", np.max(ma_profits))
print("Worst Loss:", np.min(ma_profits))

plt.figure(figsize=(10, 5))
plt.hist(ma_profits, bins=50)
plt.title(f"Moving Average Strategy Profit Distribution ({stock})")
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.show()

# ------------------------------------
# STOP LOSS STRATEGY
# ------------------------------------
stop_loss_profits = []

for sim in range(simulations):
    prices = simulation_results[:, sim]
    buy_price = prices[0]
    sell_price = prices[-1]

    for price in prices:
        if price <= buy_price * stop_loss_threshold:
            sell_price = price
            break

    profit = sell_price - buy_price
    stop_loss_profits.append(profit)

print("\nSTOP LOSS STRATEGY RESULTS:")
print("Average Profit:", np.mean(stop_loss_profits))
print("Best Profit:", np.max(stop_loss_profits))
print("Worst Loss:", np.min(stop_loss_profits))

plt.figure(figsize=(10, 5))
plt.hist(stop_loss_profits, bins=50)
plt.title(f"Stop Loss Strategy Profit Distribution ({stock})")
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.show()

# ------------------------------------
# FINAL STRATEGY COMPARISON
# ------------------------------------
strategy_names = ["Buy and Hold", "Moving Average", "Stop Loss"]
average_profits = [
    np.mean(buy_and_hold_profits),
    np.mean(ma_profits),
    np.mean(stop_loss_profits)
]
worst_losses = [
    np.min(buy_and_hold_profits),
    np.min(ma_profits),
    np.min(stop_loss_profits)
]

# Average profit comparison
plt.figure(figsize=(10, 5))
plt.bar(strategy_names, average_profits)
plt.title(f"Average Profit Comparison of Trading Strategies ({stock})")
plt.xlabel("Strategy")
plt.ylabel("Average Profit")
plt.show()

# Worst loss comparison
plt.figure(figsize=(10, 5))
plt.bar(strategy_names, worst_losses)
plt.title(f"Worst Loss Comparison of Trading Strategies ({stock})")
plt.xlabel("Strategy")
plt.ylabel("Worst Loss")
plt.show()
