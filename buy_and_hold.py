def buy_and_hold(data, initial_capital=10000):
    # Calculate the buy-and-hold portfolio value
    buy_price = data[0]
    portfolio_value = initial_capital * (data / buy_price)

    return portfolio_value
