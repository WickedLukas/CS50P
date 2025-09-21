# StockCLI
#### Video Demo: https://youtu.be/uodce1HCTK0

A simple CLI tool for key stock metrics, historical price charts, and portfolio management.

## Features

* View key stock metrics for a given stock or portfolio.
* Get historical price charts for the last week, month or year for a given stock or portfolio.
* Setup a custom portfolio.
* API caching to reduce costs and provide optimal response times as well as scalability.

## Installation

Install the required libraries from the *requirement.txt* file by executing the following terminal command from the projects root directory.
```bash
pip install -r requirements.txt
```

## Configuration

The *config.toml* file stores the configuration of the tool in the TOML format.
>**Note:** A custom filename and filepath can be specified through the command-line.

Insert the API key for the API service given by the URL. Enter the API update hours to specify when the cached data shall be updated.
>**Note:** Low values will result in more up to date data at the cost of more frequent API requests.

The maximum portfolio size and the directories where the plot and cache files are stored can also be customized.

Besides the configuration file is used to store the stock ticker symbols which are currently included in the portfolio. While it can be edited here, it is better to use the CLI since this will prevent the user from accidentally adding wrong symbols or symbols which are not available through the API.

## Usage

The tool requires a positional argument to specify the operation mode which can be either __stock__ or __portfolio__.
* The __stock__-mode is used to lookup a single stock by passing its ticker symbol.
* Since it is cumbersome to lookup many stocks one by one, the __portfolio__-mode provides a convenient way to lookup all the stocks in the portfolio at ones. No additional arguments are required for this but at first the investment portfolio needs to be setup using the positional arguments __add__ or __remove__, followed by a stock ticker symbol. The __show__ argument will print the current portfolio content.

In both modes the __-p__ or __--plot__ option can be passed to store historical price charts. By default it will generate price charts for the last month. However, an additional argument can be used for different time periods (__w__: week, __m__: month, __y__: year).

## API functions

The following API functions are implemented:
* __LISTING:__ Receive a list of available stock ticker symbols and names. It is used to check the symbols input by the user, since API calls with wrong or not available symbols would be wasted.
* __GLOBAL_QUOTE:__ Provide key stock metrics like price and percentual price change.
* __TIME_SERIES_DAILY:__ Get historical stock price data for the price charts.

## API caching

Since many APIs have usage based pricing or rate limits this tool includes a time-based caching mechanism to reduce the number of API requests. Caching also provides faster repsonse times and helps with scalability since cached responses can serve many users preventing bottlnecks on the API side.

The response of each API request is stored in a separate file within the cache directory. For repeated requests the cached data will be used until the configured API update time has passed. Therefore, every time the cached data is written or updated, the current date time for this API request is stored within the *_state.toml* file inside the cache directory.
