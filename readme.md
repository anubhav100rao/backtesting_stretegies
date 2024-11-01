# Buy and Hold Strategy

This project implements a simple "Buy and Hold" investment strategy using historical stock data. The strategy involves buying a stock at the beginning of a period and holding it until the end of the period, regardless of any fluctuations in the stock price.

## Functionality

The main functions in this project include:

-   [`get_data(ticker, start_date, end_date)`](<command:_github.copilot.openSymbolFromReferences?%5B%22get_data(ticker%2C%20start_date%2C%20end_date)%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2Fanubhav100rao%2Fdevelopment%2Fbacktesting_strategies%2Fmain.py%22%2C%22external%22%3A%22file%3A%2F%2F%2FUsers%2Fanubhav100rao%2Fdevelopment%2Fbacktesting_strategies%2Fmain.py%22%2C%22path%22%3A%22%2FUsers%2Fanubhav100rao%2Fdevelopment%2Fbacktesting_strategies%2Fmain.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A13%2C%22character%22%3A4%7D%7D%5D%5D> "Go to definition"): Fetches historical stock data for a given ticker symbol and date range.
-   [`apply_strategy(data)`](<command:_github.copilot.openSymbolFromReferences?%5B%22apply_strategy(data)%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2Fanubhav100rao%2Fdevelopment%2Fbacktesting_strategies%2Fmain.py%22%2C%22external%22%3A%22file%3A%2F%2F%2FUsers%2Fanubhav100rao%2Fdevelopment%2Fbacktesting_strategies%2Fmain.py%22%2C%22path%22%3A%22%2FUsers%2Fanubhav100rao%2Fdevelopment%2Fbacktesting_strategies%2Fmain.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A7%2C%22character%22%3A21%7D%7D%5D%5D> "Go to definition"): Applies moving average strategy to the fetched data.
-   [`backtest(signals)`](<command:_github.copilot.openSymbolFromReferences?%5B%22backtest(signals)%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2Fanubhav100rao%2Fdevelopment%2Fbacktesting_strategies%2Fmain.py%22%2C%22external%22%3A%22file%3A%2F%2F%2FUsers%2Fanubhav100rao%2Fdevelopment%2Fbacktesting_strategies%2Fmain.py%22%2C%22path%22%3A%22%2FUsers%2Fanubhav100rao%2Fdevelopment%2Fbacktesting_strategies%2Fmain.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A5%2C%22character%22%3A5%7D%7D%5D%5D> "Go to definition"): Runs a backtest on the strategy signals, including transaction costs.
-   [`calculate_metrics(portfolio)`](<command:_github.copilot.openSymbolFromReferences?%5B%22calculate_metrics(portfolio)%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2Fanubhav100rao%2Fdevelopment%2Fbacktesting_strategies%2Fmain.py%22%2C%22external%22%3A%22file%3A%2F%2F%2FUsers%2Fanubhav100rao%2Fdevelopment%2Fbacktesting_strategies%2Fmain.py%22%2C%22path%22%3A%22%2FUsers%2Fanubhav100rao%2Fdevelopment%2Fbacktesting_strategies%2Fmain.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A6%2C%22character%22%3A19%7D%7D%5D%5D> "Go to definition"): Calculates performance metrics for the backtested portfolio.
-   [`plot_results(signals, portfolio)`](<command:_github.copilot.openSymbolFromReferences?%5B%22plot_results(signals%2C%20portfolio)%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2Fanubhav100rao%2Fdevelopment%2Fbacktesting_strategies%2Fmain.py%22%2C%22external%22%3A%22file%3A%2F%2F%2FUsers%2Fanubhav100rao%2Fdevelopment%2Fbacktesting_strategies%2Fmain.py%22%2C%22path%22%3A%22%2FUsers%2Fanubhav100rao%2Fdevelopment%2Fbacktesting_strategies%2Fmain.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A8%2C%22character%22%3A22%7D%7D%5D%5D> "Go to definition"): Plots the results of the strategy and backtest.

### [`get_data(ticker, start_date, end_date)`](<command:_github.copilot.openSymbolFromReferences?%5B%22get_data(ticker%2C%20start_date%2C%20end_date)%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2Fanubhav100rao%2Fdevelopment%2Fbacktesting_strategies%2Fmain.py%22%2C%22external%22%3A%22file%3A%2F%2F%2FUsers%2Fanubhav100rao%2Fdevelopment%2Fbacktesting_strategies%2Fmain.py%22%2C%22path%22%3A%22%2FUsers%2Fanubhav100rao%2Fdevelopment%2Fbacktesting_strategies%2Fmain.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A13%2C%22character%22%3A4%7D%7D%5D%5D> "Go to definition")

Fetches historical stock data for a given ticker symbol and date range.

-   **Parameters:**

    -   [`ticker`](command:_github.copilot.openSymbolFromReferences?%5B%22ticker%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2Fanubhav100rao%2Fdevelopment%2Fbacktesting_strategies%2Fmain.py%22%2C%22external%22%3A%22file%3A%2F%2F%2FUsers%2Fanubhav100rao%2Fdevelopment%2Fbacktesting_strategies%2Fmain.py%22%2C%22path%22%3A%22%2FUsers%2Fanubhav100rao%2Fdevelopment%2Fbacktesting_strategies%2Fmain.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A13%2C%22character%22%3A13%7D%7D%5D%5D "Go to definition"): The stock ticker symbol (e.g., "^GSPC" for S&P 500).
    -   [`start_date`](command:_github.copilot.openSymbolFromReferences?%5B%22start_date%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2Fanubhav100rao%2Fdevelopment%2Fbacktesting_strategies%2Fmain.py%22%2C%22external%22%3A%22file%3A%2F%2F%2FUsers%2Fanubhav100rao%2Fdevelopment%2Fbacktesting_strategies%2Fmain.py%22%2C%22path%22%3A%22%2FUsers%2Fanubhav100rao%2Fdevelopment%2Fbacktesting_strategies%2Fmain.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A13%2C%22character%22%3A21%7D%7D%5D%5D "Go to definition"): The start date for the data fetch (e.g., "2010-01-01").
    -   [`end_date`](command:_github.copilot.openSymbolFromReferences?%5B%22end_date%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2Fanubhav100rao%2Fdevelopment%2Fbacktesting_strategies%2Fmain.py%22%2C%22external%22%3A%22file%3A%2F%2F%2FUsers%2Fanubhav100rao%2Fdevelopment%2Fbacktesting_strategies%2Fmain.py%22%2C%22path%22%3A%22%2FUsers%2Fanubhav100rao%2Fdevelopment%2Fbacktesting_strategies%2Fmain.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A13%2C%22character%22%3A33%7D%7D%5D%5D "Go to definition"): The end date for the data fetch (e.g., "2020-01-01").

-   **Returns:**
    -   A pandas DataFrame containing the 'Close' prices for the specified date range.

## Example Usage

```python
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from backtest import backtest
from metric import calculate_metrics
from strategy import apply_strategy
from visualize import plot_results

# Fetch historical data
def get_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data['Close']  # Return only the 'Close' price for simplicity

# Set parameters for the data fetch
ticker = "^GSPC"
start_date = "2010-01-01"
end_date = "2020-01-01"

# Get the data and preview it
data = get_data(ticker, start_date, end_date)

# Apply the Buy and Hold strategy
signals = apply_strategy(data)

# Re-run the backtest with transaction costs
portfolio = backtest(signals)
metrics = calculate_metrics(portfolio)
print("\nPerformance Metrics with Transaction Costs:")
for metric, value in metrics.items():
    print(f"{metric}: {value:.2%}")

# Plot the results
plot_results(signals, portfolio)
```

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/anubhav100rao/backtesting_stretegies.git
    ```
2. Navigate to the project directory:
    ```sh
    cd backtesting_strategies
    ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Chill, I got this. I'll take it from here.
