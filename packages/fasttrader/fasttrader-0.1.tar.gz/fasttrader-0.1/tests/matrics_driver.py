import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core.matrics import *

win_loss_percents = np.array([0.1, -0.2, 0.05, 1, 0.15, -0.1, -1, 0.2], dtype=np.float64)

def test_calculate_expectancy():
    expectancy = calculate_expectancy(win_loss_percents)

    print(f"Expectancy: {expectancy}")
    print(f"Expected expectancy: {np.mean(win_loss_percents)}")
    # assert expectancy == np.mean(win_loss_percents)

def test_calculate_variance():
    expectancy = calculate_expectancy(win_loss_percents)
    variance = calculate_variance(expectancy, win_loss_percents)

    print(f"Expectancy: {expectancy}")
    print(f"Variance: {variance}")
    print(f"Expected variance: {np.var(win_loss_percents)}")
    # assert variance == np.var(win_loss_percents)

def test_calculate_sharpe_ratio():
    expectancy = calculate_expectancy(win_loss_percents)
    variance = calculate_variance(expectancy, win_loss_percents)
    sharpe_ratio = calculate_sharpe_ratio(expectancy, variance)

    print(f"Expectancy: {expectancy}")
    print(f"Variance: {variance}")
    print(f"Sharpe Ratio: {sharpe_ratio}")

def runner():
    print("Running expectancy...")
    test_calculate_expectancy()
    print("\nRunning variance...")
    test_calculate_variance()
    print("\nRunning sharpe ratio...")
    test_calculate_sharpe_ratio()

runner()