import numpy as np


def calculate_metrics(portfolio):
    # Total return
    total_return = portfolio['total'][-1] / portfolio['total'][0] - 1

    # Annualized return
    trading_days = 252
    annualized_return = (
        1 + total_return) ** (trading_days / len(portfolio)) - 1

    # Annualized volatility
    annualized_volatility = portfolio['returns'].std() * np.sqrt(trading_days)

    # Sharpe ratio
    risk_free_rate = 0.01  # Assume a 1% risk-free rate
    sharpe_ratio = (annualized_return - risk_free_rate) / annualized_volatility

    # Max drawdown
    cumulative_returns = (1 + portfolio['returns']).cumprod()
    peak = cumulative_returns.cummax()
    drawdown = (cumulative_returns - peak) / peak
    max_drawdown = drawdown.min()

    metrics = {
        "Total Return": total_return,
        "Annualized Return": annualized_return,
        "Annualized Volatility": annualized_volatility,
        "Sharpe Ratio": sharpe_ratio,
        "Max Drawdown": max_drawdown
    }

    return metrics
