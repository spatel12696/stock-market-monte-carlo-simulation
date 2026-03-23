# stock-market-monte-carlo-simulation

Monte Carlo simulation project analyzing stock market risk and comparing trading strategies using Python and historical stock data.

# Monte Carlo Simulation of Stock Market Risk

This project uses Monte Carlo simulation to model possible future stock price movements and evaluate trading strategies.

## Objective

The goal of this project is to simulate future stock price paths using historical market data and analyze the performance of different trading strategies under uncertainty.

## Supported Stocks

The program allows the user to choose one of the following stock ticker symbols:

- AAPL
- TSLA
- MSFT
- AMZN

If the user presses **Enter** without typing anything, the program uses **AAPL** as the default stock.

## Data Source

Historical stock data is downloaded using the Yahoo Finance API through the `yfinance` Python library.

## Methodology

1. Download historical stock price data.
2. Calculate daily returns and volatility.
3. Use Monte Carlo simulation to generate 1000 possible future price paths.
4. Analyze the distribution of future stock prices.
5. Evaluate three trading strategies:
   - Buy and Hold
   - Moving Average Strategy
   - Stop Loss Strategy
6. Compare the strategies using average profit and worst-case loss.

## Strategies Compared

### Buy and Hold
The stock is purchased at the current price and held until the end of the simulation period.

### Moving Average Strategy
Trading decisions are based on the crossover of short-term and long-term moving averages.

### Stop Loss Strategy
The position is automatically sold if the price drops below a specified threshold to limit losses.

## Outputs

The program generates the following visualizations:

- Monte Carlo simulation of future stock prices
- Distribution of simulated final prices
- Profit distribution for Buy and Hold strategy
- Profit distribution for Moving Average strategy
- Profit distribution for Stop Loss strategy
- Strategy performance comparison charts

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- yFinance

## Requirements

Make sure Python 3 is installed on your system.

You can check by running:

```bash
python --version
```

or

```bash
python3 --version
```

## Installation

Install the required Python libraries before running the project:

```bash
pip install pandas numpy matplotlib yfinance
```

If `pip` does not work, try:

```bash
python -m pip install pandas numpy matplotlib yfinance
```

## Files

The main file for this project is:

```bash
main.py
```

## How to Run

1. Open the project folder in Visual Studio Code or in your terminal.
2. Make sure the required libraries are installed.
3. Run the program using:

```bash
python main.py
```

4. When prompted, enter one of the following stock ticker symbols:

```bash
AAPL
TSLA
MSFT
AMZN
```

5. If you just press **Enter**, the default stock `AAPL` will be used.

## Example Run

```bash
Available stock options: AAPL, TSLA, MSFT, AMZN
Enter stock ticker symbol (press Enter for AAPL): MSFT
```

## Notes

- The simulation uses 252 trading days to represent one year.
- The program runs 1000 Monte Carlo simulations.
- Results will vary slightly each time because the model uses random sampling.
- If an invalid stock ticker is entered, the program will display an error and exit.

## Author

Shivam Patel
