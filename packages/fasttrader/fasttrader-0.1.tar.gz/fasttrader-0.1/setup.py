from setuptools import setup, find_packages

VERSION = '0.1'
DESCRIPTION = 'Backtesting trading strategies'
LONG_DESCRIPTION = 'FastTrader allows you to backtest your trading strategies with historical stock market data.'

# Setting up
setup(
    name="fasttrader",
    version=VERSION,
    author="CS594GROUP2",
    author_email="<johnpiapian@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['yfinance', 'pandas', 'pandas_ta', 'numpy', 'numba', 'matplotlib'],
    keywords=['python', 'yfinance', 'trading', 'backtesting', 'stock market', 'trading strategies'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)