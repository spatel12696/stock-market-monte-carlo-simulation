# stock-market-monte-carlo-simulation
Monte Carlo simulation project analyzing stock market risk and comparing trading strategies using Python and historical stock data.

# Monte Carlo Simulation of Stock Market Risk

This project uses Monte Carlo simulation to model possible future stock
price movements and evaluate trading strategies.

## Objective

The goal of this project is to simulate future stock price paths using
historical market data and analyze the performance of different trading
strategies under uncertainty.

## Data Source

Historical stock data is downloaded using the Yahoo Finance API through
the `yfinance` Python library.

## Methodology

1.  Download historical stock price data.
2.  Calculate daily returns and volatility.
3.  Use Monte Carlo simulation to generate 1000 possible future price
    paths.
4.  Analyze the distribution of future stock prices.
5.  Evaluate three trading strategies:
    -   Buy and Hold
    -   Moving Average Strategy
    -   Stop Loss Strategy

## Strategies Compared

### Buy and Hold

The stock is purchased at the current price and held until the end of
the simulation period.

### Moving Average Strategy

Trading decisions are based on the crossover of short-term and long-term
moving averages.

### Stop Loss Strategy

The position is automatically sold if the price drops below a specified
threshold to limit losses.

## Outputs

The program generates the following visualizations:

-   Monte Carlo simulation of future stock prices
-   Distribution of simulated final prices
-   Profit distribution for Buy and Hold strategy
-   Profit distribution for Moving Average strategy
-   Profit distribution for Stop Loss strategy
-   Strategy performance comparison charts

## Technologies Used

-   Python
-   Pandas
-   NumPy
-   Matplotlib
-   yFinance

## How to Run

Install required libraries:

pip install pandas numpy matplotlib yfinance

Run the program:

python main.py

## Author

Shivam Patel
