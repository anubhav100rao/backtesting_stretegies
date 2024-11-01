from matplotlib import pyplot as plt


def plot_results(signals, portfolio):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

    # Plot price and moving averages
    ax1.plot(signals['price'], label='Price', color='black')
    ax1.plot(signals['short_mavg'], label='50-day MA', color='blue')
    ax1.plot(signals['long_mavg'], label='200-day MA', color='red')

    # Plot buy and sell signals
    ax1.plot(signals[signals['positions'] == 1].index,
             signals['short_mavg'][signals['positions'] == 1],
             '^', markersize=10, color='green', label='Buy Signal')
    ax1.plot(signals[signals['positions'] == -1].index,
             signals['short_mavg'][signals['positions'] == -1],
             'v', markersize=10, color='red', label='Sell Signal')
    ax1.set_title('Moving Average Crossover Strategy')
    ax1.legend()

    # Plot portfolio value over time
    ax2.plot(portfolio['total'], label='Portfolio Value', color='blue')
    ax2.set_title('Portfolio Value Over Time')
    ax2.legend()

    plt.tight_layout()
    plt.show()


