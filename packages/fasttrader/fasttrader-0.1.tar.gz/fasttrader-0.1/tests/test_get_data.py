import pytest
import pandas as pd
from core import Data

@pytest.fixture
def data_instance():
    return Data()

def test_get_price_data(data_instance):
    start = pd.Timestamp('2023-07-22')
    end = pd.Timestamp('2023-08-22')
    interval = pd.Timedelta('1d')
    ticker = 'AAPL'
    df = data_instance.get_price_data(start, end, interval, ticker)

    assert not df.empty
    assert isinstance(df, pd.DataFrame)
    assert df.columns.size == 11

def test_price_data_invalid_interval(data_instance):
    start = pd.Timestamp('2023-07-22')
    end = pd.Timestamp('2023-08-22')
    interval = pd.Timedelta(seconds=1)
    ticker = 'AAPL'

    with pytest.raises(ValueError):
        data_instance.get_price_data(start, end, interval, ticker)

@pytest.mark.parametrize('start, end', [
    ('2024-08-22', '2024-07-22'),  # End date before start date
    ('2024-08-22', '2023-08-22'),  # End date in the past
    ('2023-08-22', '2025-08-22')   # End date in the future
])
def test_get_price_data_invalid_date(data_instance, start, end):
    interval = pd.Timedelta('1d')
    ticker = 'AAPL'

    with pytest.raises(ValueError):
        start_date = pd.Timestamp(start)
        end_date = pd.Timestamp(end)
        data_instance.get_price_data(start_date, end_date, interval, ticker)
