import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
import pandas_ta as pta
import matplotlib.pyplot as plt

from core.data import Data
from core.signals import SignalGenerator
from core.simulator import Simulator

# import the BubblePlotGenerator class
from core.generate_bubble_plot import BubblePlotGenerator

# DATA
# create an instance of the Data class
data_grabber = Data()

price_data = pd.read_csv('AAPL.csv', index_col='Date', parse_dates=True)
metadata = {'start': price_data.index[0], 'end': price_data.index[-1], 'interval': '1d', 'ticker': 'AAPL', 'indicator': 'SMA', "params": {'length': 20}}
ma_20 = pta.sma(price_data['Close'], 20)


# SIGNAL GENERATOR
#construct a signal generator from SignalGenerator in signals.py
strategy_instance = SignalGenerator(price_data['Close'])
strategy_instance.generate_above_below(ma_20, metadata)
strategy_output = strategy_instance.get_results()


bubble_sim = Simulator(strategy_instance, metadata)
bubble_sim.simulate()
bubble_output = bubble_sim.get_results()

# Generate the bubble plot
# bubble_plot_generator = BubblePlotGenerator(bubble_output)
bubble_plot_generator = BubblePlotGenerator(bubble_output, price_data.index)
bubble_plot_generator.generate_bubble_plot()
