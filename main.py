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

signals = apply_strategy(data)


# Re-run the backtest with transaction costs
portfolio = backtest(signals)
metrics = calculate_metrics(portfolio)
print("\nPerformance Metrics with Transaction Costs:")
for metric, value in metrics.items():
    print(f"{metric}: {value:.2%}")

# Plot the results
plot_results(signals, portfolio)
