import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core.signals import SignalGenerator

signal_generator = SignalGenerator()

entry_probability = .5
exit_probability = .5
array_size = 20

result = signal_generator.random_signals(array_size, entry_probability, exit_probability)

print(f'Example of a random trading strategy on an array of size {array_size}:\n')
print(result)
