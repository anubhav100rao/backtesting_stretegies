import pandas as pd


def backtest(signals, initial_capital=10000, transaction_cost=0.001):
    # Set up the initial portfolio
    positions = pd.DataFrame(index=signals.index).fillna(0.0)
    portfolio = pd.DataFrame(index=signals.index)

    # Buy or sell 1 unit of the asset on each signal
    positions['holdings'] = signals['positions'].cumsum() * signals['price']

    # Calculate transaction costs
    trade_costs = signals['positions'].abs(
    ) * signals['price'] * transaction_cost

    # Calculate portfolio value over time, deducting transaction costs
    portfolio['holdings'] = positions['holdings']
    portfolio['cash'] = initial_capital - \
        (signals['positions'] * signals['price']
         ).cumsum() - trade_costs.cumsum()
    portfolio['total'] = portfolio['cash'] + portfolio['holdings']
    portfolio['returns'] = portfolio['total'].pct_change()

    return portfolio



