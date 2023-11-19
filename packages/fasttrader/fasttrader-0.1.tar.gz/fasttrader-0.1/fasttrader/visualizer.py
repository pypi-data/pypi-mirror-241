import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class Visualizer:

    def __init__(self) -> None:
        pass

    def visualize_strategy(self, price_data, trading_signals, win_loss_percents, portfolio_values):
        self.generate_line_plot(price_data, portfolio_values, trading_signals)
        self.generate_bubble_plot(win_loss_percents, price_data)


