# Forex-Algo

Automated trading and analysis framework for Forex markets, featuring data collection, technical analysis, backtesting, and live trading capabilities.
## Features

- **Automated Trading Bot**: Modular bot for executing trades based on technical strategies.
- **OANDA API Integration**: Fetches real-time and historical data.
- **Technical Analysis**: Moving averages, MACD, RSI, and more.
- **Backtesting & Simulation**: Test strategies on historical data.
- **Data Management**: Efficient storage and retrieval of market data.
- **Logging & Monitoring**: Detailed logs for trades and errors.
- **Jupyter Notebooks**: Exploration and visualization tools for research and prototyping.
## Project Structure

```text
api/                # OANDA API integration
bot/                # Trading bot logic and managers
constants/          # Definitions and constants
data/               # Market data (pkl, json, etc.)
exploration/        # Jupyter notebooks for research
infrastructure/     # Data collection, logging, and utilities
logs/               # Log files
models/             # ML models or data models (if any)
simulation/         # Backtesting and simulation scripts
stream_example/     # Streaming data examples
technicals/         # Technical indicator implementations
main.py             # Main entry point
run_bot.py          # Script to run the trading bot
api_tests.py        # API test scripts
README.md           # Project documentation
## Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/SpaciousFish/Forex-Algo.git
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   *(If `requirements.txt` is missing, install packages as needed for pandas, numpy, requests, etc.)*

### Configuration
- Update `bot/settings.json` with your OANDA API credentials and trading preferences.

### Running the Bot
### Running Tests

```sh
python api_tests.py

### Data Collection
Collect new data using:
```sh
python infrastructure/collect_data.py
## Notebooks

Explore and analyze strategies in the `exploration/` folder using Jupyter:
```sh
jupyter notebook exploration/

## Logging
- Logs are stored in the `logs/` directory for debugging and monitoring.

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](LICENSE)
# Forex-Algo
