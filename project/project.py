# CS50P - Final Project
# StockCLI - A simple CLI tool for key stock metrics, historical price charts, and portfolio management.

import sys
import argparse
import requests
import toml
import json
import csv
import re

from datetime import datetime, timedelta
from pathlib import Path
from tabulate import tabulate
import pandas as pd
import matplotlib.pyplot as plt


class StockApi:
    """Get stock data from an API.

    The data is cached for a configured duration in order to save API requests.

    Attributes:
        __config: Config parameters.
        __cache: Directory where the cached data is stored.
        __state: Instance of State which manages if the cached data needs to be updated.
        __listing: Listing data from the API. It contains symbols and names of the available stock.
          It is used to get names for the symbols and to avoid API requests with symbols which are not available.
    """

    def __init__(self, config: dict):
        self.__config = config

        self.__cache_dir = Path(config["cache_directory"])
        if not self.__cache_dir.exists():
            self.__cache_dir.mkdir(parents=True, exist_ok=True)

        state_file = self.__cache_dir / "_state.toml"
        self.__state = self.State(state_file, config["url"])
        self.__listing = self.__get_listing()

    def get(self, params: dict) -> dict:
        """Get data from the API (or cache)."""

        self.get_listing(params["symbol"])

        table, table_element = self.__state.get_table_info(params)
        request_datetime = self.__state.get_request_datetime(table, table_element)

        data = {}
        current_datetime = datetime.now()
        elapsed_time = abs(current_datetime - request_datetime)
        cache_file: Path = Path(self.__cache_dir) / (
            table + "__" + table_element + ".json"
        )
        if elapsed_time < timedelta(hours=self.__config["api_update_hours"]):
            data = self.__get_cache_data(cache_file)

        if not data:
            data = self.__get_api_data(params)

            with open(cache_file, "w") as json_file:
                json.dump(data, json_file)

            self.__state.update_request_datetime(table, table_element, current_datetime)

        return data

    def get_listing(self, symbol: str) -> dict:
        """Get listing from the API (or cache) and extract the data for the passed symbol."""

        symbol = symbol.upper()
        listing_symbol = next(
            filter(
                lambda listing_symbol: listing_symbol["symbol"] == symbol,
                self.__listing,
            ),
            None,
        )
        if listing_symbol is None:
            sys.exit(f"Unknown ticker symbol {symbol}")

        return listing_symbol

    def __get_listing(self) -> list[dict]:
        params = {"function": "LISTING_STATUS", "apikey": self.__config["api_key"]}

        table, table_element = self.__state.get_table_info(params)
        request_datetime = self.__state.get_request_datetime(table, table_element)

        listing = None
        current_datetime = datetime.now()
        elapsed_time = abs(current_datetime - request_datetime)
        cache_file: Path = Path(self.__cache_dir) / (
            "_" + table + "__" + table_element + ".json"
        )
        if elapsed_time < timedelta(hours=self.__config["api_update_hours"]):
            listing = self.__get_cache_listing(cache_file)

        if not listing:
            listing = self.__get_api_listing(params)

            with open(cache_file, "w") as file:
                writer = csv.DictWriter(file, listing[0].keys())
                writer.writeheader()
                writer.writerows(listing)

            self.__state.update_request_datetime(table, table_element, current_datetime)

        return listing

    def __get_cache_listing(self, cache_file: Path) -> list[dict]:
        listing = []
        try:
            with open(cache_file, "r") as file:
                listing = list(csv.DictReader(file))
        except FileNotFoundError:
            pass
        except Exception:
            print("Could not read", cache_file.resolve())

        return listing

    def __get_api_listing(self, params: dict) -> list[dict]:
        with requests.Session() as session:
            try:
                response = session.get(self.__config["url"], params=params)
                response.raise_for_status()
            except requests.HTTPError:
                sys.exit(f"Could not complete {params["function"]} request!")

        decoded_content = response.content.decode("utf-8")
        listing_status = list(
            csv.DictReader(decoded_content.splitlines(), delimiter=",")
        )

        listing = []
        for element in listing_status:
            listing.append(
                {
                    key: value.strip()
                    for key, value in element.items()
                    if key not in ["ipoDate", "delistingDate", "status"]
                }
            )

        return listing

    def __get_cache_data(self, cache_file: Path) -> dict:
        data = {}
        try:
            with open(cache_file, "r") as json_file:
                data = json.load(json_file)
        except Exception:
            print("Could not read", cache_file.resolve())

        return data

    def __get_api_data(self, params: dict) -> dict:
        if "apikey" not in params:
            params["apikey"] = self.__config["api_key"]

        try:
            response = requests.get(self.__config["url"], params)
            response.raise_for_status()
        except requests.HTTPError:
            sys.exit(f"Could not complete {params["function"]} request")

        return response.json()

    class State:
        """Manages if the cached data needs to be updated.

        Args:
            state_file: Path to the state file.
            url: URL of the API.
        Attributes:
            __state_file: Path to the state file.
            __api_service: Name of the API service extracted from the URL.
            __state: Stores when which API request has been performed.
        """

        def __init__(self, state_file: Path, url: str):
            self.__state_file = state_file

            pattern = r"https?://(?:www\.)?(?P<api_service>.+?)\.|="
            if match := re.search(pattern, url):
                self.__api_service = match.group("api_service")
            else:
                sys.exit(f"No API service matched for {url}")

            self.__state = self.__read_state()

        def get_table_info(self, params: dict) -> tuple[str, str]:
            """Get table info required for saving when which API request has been performed."""

            if params["function"] == "LISTING_STATUS":
                table = "LISTING"
                clean = ["apikey", "function"]
            else:
                table = params["symbol"]
                clean = ["apikey", "symbol"]

            params_cleaned = {
                key: value for key, value in params.items() if key not in clean
            }
            params_cleaned["api_service"] = self.__api_service
            params_cleaned = dict(sorted(params_cleaned.items()))
            values = []
            for value in params_cleaned.values():
                values.append(value)
            table_element = "__".join(values)

            return table, table_element

        def get_request_datetime(self, table: str, table_element: str) -> datetime:
            """Get the datetime of the last request identified by table and table_element."""

            request_datetime = datetime.min
            try:
                request_datetime = datetime.fromisoformat(
                    self.__state[table][table_element]
                )
            except KeyError:
                pass

            return request_datetime

        def update_request_datetime(
            self, table: str, table_element, current_datetime: datetime
        ):
            """Update the datetime of the request identified by table and table_element."""

            if table not in self.__state:
                self.__state[table] = {}
            self.__state[table][table_element] = current_datetime.isoformat()

            with open(self.__state_file, "w") as file:
                toml.dump(self.__state, file)

        def __read_state(self) -> dict:
            state = {}
            try:
                with open(self.__state_file, "r") as file:
                    state = toml.load(file)
            except FileNotFoundError:
                pass
            except Exception:
                print("Could not read", self.__state_file.resolve())

            return state


def main():
    args = parse_command_line()

    with open(Path(args.config), "r") as file:
        config = toml.load(file)

    stock_api = StockApi(config)

    if args.mode == "stock" or (
        args.mode == "portfolio"
        and (args.portfolio_cmd == "add" or args.portfolio_cmd == "remove")
    ):
        symbol = args.symbol.upper()
        if not (args.mode == "portfolio" and args.portfolio_cmd == "remove"):
            # Raise exception when symbol is not included within listing
            stock_api.get_listing(symbol)

    if args.mode == "portfolio" and args.portfolio_cmd != None:
        # Manage which stock is included in the portfolio
        if "portfolio" not in config:
            config["portfolio"] = []

        if args.portfolio_cmd != "show":
            manage_portfolio(
                symbol,
                args.portfolio_cmd,
                config["portfolio"],
                config["portfolio_max_size"],
            )
            with open(args.config, "w") as file:
                toml.dump(config, file)

        for symbol in config["portfolio"]:
            print(symbol)
        return

    if args.mode == "stock" or (
        args.mode == "portfolio" and args.portfolio_cmd == None
    ):
        symbols = []
        if args.mode == "stock":
            symbols.append(symbol)
        elif args.mode == "portfolio":
            symbols = config["portfolio"]

        stock_infos = get_stock_infos(symbols, stock_api)

        # Print infos for the passed stock ticker symbol or the portfolio
        print(tabulate(stock_infos, headers="keys", tablefmt="grid"))

        if args.plot != None:
            time_period = get_time_period(args.plot)

            stock_histories = get_stock_histories(symbols, stock_api)

            plot_dir = Path(config["plot_directory"])
            if not plot_dir.exists():
                plot_dir.mkdir(parents=True, exist_ok=True)

            for stock_history, stock_info, symbol in zip(
                stock_histories, stock_infos, symbols
            ):
                df_close = extract_data(stock_history, time_period, "4. close")

                # Store plots for the passed stock ticker symbol or the portfolio
                plt.figure(figsize=(8, 5))
                plt.plot(df_close.index, df_close)
                plt.title(f"{stock_info["Name"]} ({stock_info["Symbol"]})")
                plt.xlabel("Date")
                plt.ylabel("USD")
                plt.grid(True)
                plt.tight_layout()
                plt.savefig(plot_dir / f"plot_{stock_info["Symbol"]}_{args.plot}.png")


def parse_command_line() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Output key stock metrics and price plots for a given stock or your stock portfolio"
    )

    subparsers = parser.add_subparsers(dest="mode", required=True)

    # Stock mode
    stock_parser = subparsers.add_parser("stock", help="Lookup stock")
    stock_parser.add_argument("symbol", help="Stock ticker symbol")
    add_plot_arg(stock_parser)
    add_config_arg(stock_parser)

    # Portfolio mode
    portfolio_parser = subparsers.add_parser(
        "portfolio",
        help="Manage or lookup your stock portfolio",
        description=(
            "Process portfolio, if called without a subcommand.\n"
            "The --plot option is only available in this mode."
        ),
    )
    add_plot_arg(portfolio_parser)
    add_config_arg(portfolio_parser)

    # Manage portfolio using subcommands
    portfolio_subparsers = portfolio_parser.add_subparsers(
        dest="portfolio_cmd", required=False
    )

    show_parser = portfolio_subparsers.add_parser(
        "show", help="Show all symbols in the portfolio"
    )
    add_config_arg(show_parser)

    add_parser = portfolio_subparsers.add_parser(
        "add", help="Add a symbol to the portfolio"
    )
    add_parser.add_argument("symbol", help="Stock ticker symbol to add")
    add_config_arg(add_parser)

    remove_parser = portfolio_subparsers.add_parser(
        "remove", help="Remove a symbol from the portfolio"
    )
    remove_parser.add_argument("symbol", help="Stock ticker symbol to remove")
    add_config_arg(remove_parser)

    return parser.parse_args()


def add_plot_arg(parser: argparse.ArgumentParser):
    parser.add_argument(
        "-p",
        "--plot",
        nargs="?",
        const="m",
        choices=["w", "m", "y"],
        help="Plot range: w=week, m=month, y=year (default: m)",
    )


def add_config_arg(parser: argparse.ArgumentParser):
    parser.add_argument(
        "-c",
        "--config",
        default="config.toml",
        help="Config TOML (default: %(default)s)",
    )


def manage_portfolio(symbol: str, portfolio_cmd: str, portfolio: list, max_count: int):
    """Manage portfolio by adding or removing stock. Adding is limited up to max_count."""

    if portfolio_cmd not in ("add", "remove"):
        raise ValueError("Unknown protfolio command")

    if portfolio_cmd == "add":
        if symbol not in portfolio:
            if len(portfolio) > max_count - 1:
                sys.exit(
                    f"Failed to add symbol, because the maximum portfolio size is {max_count}."
                )
            portfolio.append(symbol)
            portfolio.sort()
    elif portfolio_cmd == "remove":
        if symbol in portfolio:
            portfolio.remove(symbol)


def get_stock_infos(symbols: list[str], stock_api: StockApi) -> list[dict]:
    "Get stock info for the passed symbols."

    stock_infos = []
    for symbol in symbols:
        params = {"function": "GLOBAL_QUOTE", "symbol": symbol}

        stock_listing = stock_api.get_listing(symbol)
        stock_global_quote = stock_api.get(params)
        stock_info = parse_stock_info(stock_listing, stock_global_quote)
        stock_infos.append(stock_info)
    return stock_infos


def parse_stock_info(listing: dict, global_quote: dict) -> dict:
    """Parse the relevant stock info."""
    data = global_quote["Global Quote"]
    return {
        "Name": listing["name"],
        "Symbol": data["01. symbol"],
        "Price": f"{float(data["05. price"]):.2f} USD",
        "Change": data["10. change percent"],
    }


def get_stock_histories(symbols: list[str], stock_api: StockApi) -> list[dict]:
    """Get stock histories for the passed symbols."""

    stock_histories = []
    for symbol in symbols:
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "outputsize": "full",
        }

        stock_history = stock_api.get(params)
        stock_histories.append(stock_history)
    return stock_histories


def get_time_period(plot_arg: str) -> pd.DateOffset | pd.Timedelta:
    """Get time period for the passed plot command line argument."""

    match plot_arg:
        case "w":
            return pd.Timedelta(weeks=1)
        case "m":
            return pd.DateOffset(months=1)
        case "y":
            return pd.DateOffset(years=1)
        case _:
            raise ValueError(f"Unknown plot argument '{plot_arg}'")


def extract_data(
    stock_history: dict, time_period: pd.DateOffset | pd.Timedelta, name: str
) -> pd.DataFrame:
    """Extract history data for the passed time period"""

    df = pd.DataFrame.from_dict(stock_history["Time Series (Daily)"], orient="index")
    df.index = pd.to_datetime(df.index)

    ds_close = df[df.index >= (df.index.max() - time_period)][name]
    ds_close = ds_close.apply(pd.to_numeric)
    return ds_close


if __name__ == "__main__":
    main()
