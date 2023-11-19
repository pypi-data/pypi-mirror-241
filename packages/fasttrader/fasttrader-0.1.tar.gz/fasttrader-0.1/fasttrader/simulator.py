import numpy as np
import pandas as pd
import numba as nb 

# HELPER FUNCTIONS
@nb.jit(nopython=True)
def win_loss_loop(trading_signals, price_data, starting_cash) -> dict:
    win_loss = np.zeros_like(price_data)
    win_loss_percents = np.zeros_like(price_data)
    portfolio_values = np.empty_like(price_data)

    portfolio_values[0] = starting_cash # setting starting portfolio value

    for i in range(trading_signals.size):
        if i > 0:
            portfolio_values[i] = portfolio_values[i - 1]

        # if trading signal is positive, store the entry price and starting portfolio value
        if trading_signals[i] > 0:
            entry_price = price_data[i]
            entry_portfolio_value = portfolio_values[i]

        # if trading signal is negative, compare the entry and exit prices and portfolio values and store in arrays
        if trading_signals[i] < 0:
            win_loss_percents[i] = price_data[i] / entry_price
            portfolio_values[i] = win_loss_percents[i] * entry_portfolio_value
            win_loss_percents[i] -= 1
            win_loss[i] = portfolio_values[i] - entry_portfolio_value
        
    output = {
        "win_loss": win_loss,
        "win_loss_percents": win_loss_percents,
        "portfolio_values": portfolio_values
    }

    return output

@nb.jit(nopython=True)
def calculate_expectancy(win_loss_percents) -> float:
    """
    Calculate the expectancy of a list of win-loss percentages.

    This function takes a list of win-loss percentages as input, where values range
    from -1 to 1 (or more) representing percentage, with 0 representing no trade. 
    It calculates the expectancy by summing the non-zero percentages and dividing
    by the number of trades.

    Parameters:
    win_loss_percents (numpy.ndarray): win-loss percentages.

    Returns:
    float: The calculated expectancy, or None if the input list is empty.
    """

    if len(win_loss_percents) == 0:
        return 0

    non_zero_percentages = win_loss_percents[win_loss_percents != 0]
    total_returns = np.sum(non_zero_percentages)
    number_of_trades = len(non_zero_percentages)

    if number_of_trades == 0:
        return 0

    expectancy = total_returns / number_of_trades

    return np.float64(expectancy)

@nb.jit(nopython=True)
def calculate_variance(expectancy, win_loss_percents) -> float:
    """
    Calculate the variance of a list of win-loss percentages.

    This function calculates the variance of a list of win-loss percentages, taking into account the expectancy (mean).
    The variance measures the degree of dispersion or spread of the values around the mean. A higher variance means 
    greater variability or dispersion in the dataset.

    Parameters:
    expectancy (float): The mean or expectancy of the win-loss percentages.
    win_loss_percents (numpy.ndarray): A list of win-loss percentages, including zero values.

    Returns:
    float: The calculated variance or None if the input list is empty or contains no non-zero values.
    """

    if not expectancy or len(win_loss_percents) == 0:
        return None

    non_zero_percentages = win_loss_percents[win_loss_percents != 0]
    number_of_trades = len(non_zero_percentages)

    if number_of_trades == 0:
        return None

    variance = np.sum((non_zero_percentages - expectancy) ** 2) / number_of_trades

    return np.float64(variance)

@nb.jit(nopython=True)
def calculate_sharpe_ratio(expectancy, variance, risk_free_rate):
    """
    Calculate the Sharpe Ratio for a given investment or trading strategy.

    The Sharpe Ratio assesses the risk-adjusted returns of an investment or trading strategy.
    It is calculated as the difference between the expected return and the risk-free rate, divided by the standard deviation of returns.

    Parameters:
    expectancy (float): the mean or expectancy of the win-loss percentages.
    variance (float): The variance of returns or portfolio values.
    risk_free_rate (float): The risk-free rate of return, typically representing a Treasury yield.

    Returns:
    float: The calculated Sharpe Ratio, which measures risk-adjusted performance, or None if the input(s) is empty.
    """

    if not expectancy or not variance:
        return None

    sharpe_ratio = (expectancy - risk_free_rate) / np.sqrt(variance)

    return np.float64(sharpe_ratio)

@nb.jit(nopython=True)
def calculate_max_drawdown(win_loss_percents_np) -> float:
    """Calculates the maximum drawdown for a given list of win/loss percentages.

    Args:
        win_loss_percents_np (np.array): A numpy array of win/loss percentages.

    Returns:
        float: The maximum drawdown.
    """
    max_drawdown = 0

    for i in range(len(win_loss_percents_np)):
        max_drawdown = min(max_drawdown, win_loss_percents_np[i])

    return max_drawdown

@nb.jit(nopython=True)
def calculate_ratio_winning_trades(win_loss_percents_np) -> float:
    """Calculates the ratio of winning trades for a given list of win/loss percentages.

    Args:
        win_loss_percents_np (np.array): A numpy array of win/loss percentages.

    Returns:
        float: The ratio of winning trades.
    """
    num_winning_trades = 0
    num_losing_trades = 0

    for i in range(len(win_loss_percents_np)):
        if win_loss_percents_np[i] > float(0):
            num_winning_trades += 1
        elif win_loss_percents_np[i] < float(0):
            num_losing_trades += 1

    if num_losing_trades == 0:
        return 1
    return num_winning_trades / num_losing_trades


class Simulator:

    def __init__(self, strategy_instance, risk_free_rate, metadata=None):
        self.strategy_instance = strategy_instance
        self.risk_free_rate = risk_free_rate
        self.metadata = strategy_instance.metadata if metadata is None else metadata
        self.starting_cash = 10000
        self.win_loss_stats = None
        self.stats = None

    def simulate(self):
        """
        Simulates a trading strategy using the given trading signals and price data.
        This function uses the trading signals and price data to calculate the
        portfolio values, win/loss percentages, and win/loss values.

        Returns:
            dict: A dictionary containing the following arrays:
                max_drawdown: The maximum drawdown for the strategy
                ratio_winning_trades: The ratio of winning trades for the strategy
                sharpe_ratio: The Sharpe Ratio for the strategy
                expectancy: The expectancy for the strategy
                variance: The variance for the strategy
        """

        # generate win loss stats if not already generated
        # TODO: check if win_loss_stats is None
        self.calculate_trades_win_loss()

        # localize variables
        win_loss = self.win_loss_stats["win_loss"]
        win_loss_percents = self.win_loss_stats["win_loss_percents"]
        portfolio_values = self.win_loss_stats["portfolio_values"]

        # generate stats
        expectancy = calculate_expectancy(win_loss_percents)
        variance = calculate_variance(expectancy, win_loss_percents)
        sharpe_ratio = calculate_sharpe_ratio(expectancy, variance, self.risk_free_rate)
        max_drawdown = calculate_max_drawdown(win_loss_percents)
        ratio_winning_trades = calculate_ratio_winning_trades(win_loss_percents)

        stats = {
            "max_drawdown": max_drawdown,
            "ratio_winning_trades": ratio_winning_trades,
            "sharpe_ratio": sharpe_ratio,
            "expectancy": expectancy,
            "variance": variance
        }

        self.stats = stats

        return self.stats
    
    def calculate_trades_win_loss(self) -> dict:
        """
        Calculates the win/loss percentages and dollar amounts for a given set of trading signals and price data.

        Args:
            price_data: An array of price data to calculate the strategy on
            trading_signals: A matching array of indicators to reflect a trading strategy
            starting_cash: The starting value for the portfolio
        Returns:
            dict: A dictionary containing the following arrays:
                win_loss[]: Holds trade gain/loss in dollar amounts
                win_loss_percents[]: Holds the portfolio percent change as a result of closing trades
                portfolio_values[]: Holds the portfolio value and is only be updated on closing trades
        """

        # localize variables
        # TODO: validate that price_data and trading_signals are numpy arrays
        starting_cash = self.starting_cash
        price_data = self.strategy_instance.price_data.to_numpy()
        trading_signals = self.strategy_instance.trading_signals

        if starting_cash < 0:
            raise ValueError("starting_cash must be greater than 0")
        if len(price_data) != len(trading_signals):
            raise ValueError("price_data and trading_signals must be the same size")

        # return dict of arrays -> win_loss, win_loss_percents, portfolio_values
        output = win_loss_loop(trading_signals, price_data, starting_cash)
        self.win_loss_stats = output

        return self.win_loss_stats
    
    def get_results(self) -> dict:
        """
        Returns:
        A dict containing:
            a nested dataframe containing the following:
                win_loss_np
                win_loss_percents_np
                portfolio_values_np
            a nested dataframe containing the input to the simulation: 
                trading_signals_np
                price_data_np
            a dict containing the metadata passed in:
                metadata
            a dict containing the following:
                max_drawdown
                ratio_winning_trades
                sharpe ratio
                expectancy 
                variance
        """

        input_df = pd.DataFrame({
            "trading_signals": self.strategy_instance.trading_signals,
            "price_data": self.strategy_instance.price_data
        })

        win_loss_df = pd.DataFrame({
            "win_loss": self.win_loss_stats["win_loss"],
            "win_loss_percents": self.win_loss_stats["win_loss_percents"],
            "portfolio_values": self.win_loss_stats["portfolio_values"]
        })

        output = {
            "input": input_df,
            "win_loss": win_loss_df,
            "stats": self.stats,
            "metadata": self.metadata
        }

        return output
