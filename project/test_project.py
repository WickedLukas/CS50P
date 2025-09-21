from project import manage_portfolio, parse_stock_info, get_time_period, extract_data

import pytest
import pandas as pd
from pandas.testing import assert_series_equal


def test_manage_portfolio_add():
    """Test adding symbols to the portfolio."""

    portfolio = []
    max_count = 3
    portfolio_cmd = "add"

    symbol = "NFLX"
    manage_portfolio(symbol, portfolio_cmd, portfolio, max_count)
    assert portfolio == ["NFLX"]

    # Check if symbol is added in the correct order
    symbol = "AAPL"
    manage_portfolio(symbol, portfolio_cmd, portfolio, max_count)
    assert portfolio == ["AAPL", "NFLX"]

    # Check if adding duplicate symbols is prevented
    symbol = "AAPL"
    manage_portfolio(symbol, portfolio_cmd, portfolio, max_count)
    assert portfolio == ["AAPL", "NFLX"]

    symbol = "TSLA"
    manage_portfolio(symbol, portfolio_cmd, portfolio, max_count)
    assert portfolio == ["AAPL", "NFLX", "TSLA"]

    # Check if sys.exit() is called when attempting to add a symbol while exceeding max_count
    symbol = "AMZN"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        manage_portfolio(symbol, portfolio_cmd, portfolio, max_count)
    assert pytest_wrapped_e.type == SystemExit


def test_manage_portfolio_remove():
    """Test removing symbols from the portfolio."""

    portfolio = ["AAPL", "NFLX", "TSLA"]
    max_count = 3
    portfolio_cmd = "remove"

    symbol = "NFLX"
    manage_portfolio(symbol, portfolio_cmd, portfolio, max_count)
    assert portfolio == ["AAPL", "TSLA"]

    # Test removing a symbol not included in the portfolio
    symbol = "MCD"
    manage_portfolio(symbol, portfolio_cmd, portfolio, max_count)
    assert portfolio == ["AAPL", "TSLA"]

    symbol = "AAPL"
    manage_portfolio(symbol, portfolio_cmd, portfolio, max_count)
    assert portfolio == ["TSLA"]

    symbol = "TSLA"
    manage_portfolio(symbol, portfolio_cmd, portfolio, max_count)
    assert portfolio == []

    # Test removing a symbol from an empty list
    symbol = "AMZN"
    manage_portfolio(symbol, portfolio_cmd, portfolio, max_count)
    assert portfolio == []


def test_parse_stock_info():
    """Test parsing the relevant stock info."""

    listing = {
        "symbol": "AAPL",
        "name": "Apple Inc",
        "exchange": "NASDAQ",
        "assetType": "Stock",
    }

    global_quote = {
        "Global Quote": {
            "01. symbol": "AAPL",
            "02. open": "232.1850",
            "03. high": "232.4200",
            "04. low": "225.9500",
            "05. price": "226.7900",
            "06. volume": "83440810",
            "07. latest trading day": "2025-09-10",
            "08. previous close": "234.3500",
            "09. change": "-7.5600",
            "10. change percent": "-3.2259%",
        }
    }

    stock_info_reference = {
        "Name": "Apple Inc",
        "Symbol": "AAPL",
        "Price": f"{226.7900:.2f} USD",
        "Change": "-3.2259%",
    }

    stock_info = parse_stock_info(listing, global_quote)
    assert stock_info == stock_info_reference


def test_get_time_period():
    """Test time period for the passed plot command line argument."""

    assert get_time_period("w") == pd.Timedelta(weeks=1)
    assert get_time_period("m") == pd.DateOffset(months=1)
    assert get_time_period("y") == pd.DateOffset(years=1)
    with pytest.raises(ValueError):
        get_time_period("z")
    with pytest.raises(ValueError):
        get_time_period("3")
    with pytest.raises(ValueError):
        get_time_period("abcd123")


def test_extract_data():
    """Test if history data is correctly extracted for the passed time period"""

    # total
    stock_history = {
        "Time Series (Daily)": {
            "2025-09-10": {"test": "0.0"},
            "2025-09-09": {"test": "0.0"},
            "2025-09-02": {"test": "0.0"},
            "2025-08-15": {"test": "0.0"},
            "2025-03-12": {"test": "0.0"},
            "2024-10-16": {"test": "0.0"},
            "2024-09-05": {"test": "0.0"},
        }
    }

    # week
    stock_history_reference_w = {
        "Time Series (Daily)": {
            "2025-09-10": {"test": "0.0"},
            "2025-09-09": {"test": "0.0"},
        }
    }
    stock_history_reference_w_ds = pd.DataFrame.from_dict(
        stock_history_reference_w["Time Series (Daily)"], orient="index"
    )["test"]
    stock_history_reference_w_ds.index = pd.to_datetime(
        stock_history_reference_w_ds.index
    )
    stock_history_reference_w_ds = stock_history_reference_w_ds.apply(pd.to_numeric)
    stock_history_w_ds = extract_data(stock_history, pd.Timedelta(weeks=1), "test")
    assert_series_equal(stock_history_w_ds, stock_history_reference_w_ds)

    # month
    stock_history_reference_m = {
        "Time Series (Daily)": {
            "2025-09-10": {"test": "0.0"},
            "2025-09-09": {"test": "0.0"},
            "2025-09-02": {"test": "0.0"},
            "2025-08-15": {"test": "0.0"},
        }
    }
    stock_history_reference_m_ds = pd.DataFrame.from_dict(
        stock_history_reference_m["Time Series (Daily)"], orient="index"
    )["test"]
    stock_history_reference_m_ds.index = pd.to_datetime(
        stock_history_reference_m_ds.index
    )
    stock_history_reference_m_ds = stock_history_reference_m_ds.apply(pd.to_numeric)
    stock_history_m_ds = extract_data(stock_history, pd.DateOffset(months=1), "test")
    assert_series_equal(stock_history_m_ds, stock_history_reference_m_ds)

    # year
    stock_history_reference_y = {
        "Time Series (Daily)": {
            "2025-09-10": {"test": "0.0"},
            "2025-09-09": {"test": "0.0"},
            "2025-09-02": {"test": "0.0"},
            "2025-08-15": {"test": "0.0"},
            "2025-03-12": {"test": "0.0"},
            "2024-10-16": {"test": "0.0"},
        }
    }
    stock_history_reference_y_ds = pd.DataFrame.from_dict(
        stock_history_reference_y["Time Series (Daily)"], orient="index"
    )["test"]
    stock_history_reference_y_ds.index = pd.to_datetime(
        stock_history_reference_y_ds.index
    )
    stock_history_reference_y_ds = stock_history_reference_y_ds.apply(pd.to_numeric)
    stock_history_y_ds = extract_data(stock_history, pd.DateOffset(years=1), "test")
    assert_series_equal(stock_history_y_ds, stock_history_reference_y_ds)
