import pandas as pd

# calculate the moving average of the stock price and apply the strategy


def apply_strategy(data, short_window=50, long_window=200):
    signals = pd.DataFrame(index=data.index)
    signals['price'] = data

    # calculate the short and long moving averages
    signals['short_mavg'] = data.rolling(
        window=short_window, min_periods=1, center=False).mean()

    signals['long_mavg'] = data.rolling(
        window=long_window, min_periods=1, center=False).mean()

    # create a signal to buy or sell the stock
    signals['signal'] = 0
    signals['signal'][short_window:] = (
        (signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:]).astype(int))

    # generate trading orders
    signals['positions'] = signals['signal'].diff()
    
    return signals