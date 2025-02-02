from init import app
from jobs.stock_price import StockPrice
from jobs.symbols import Symbols

import click

# Chatgpt chrome
# @app.cli.command("greet")
# @click.argument("name")
# def greet(name):
#     """Greets the specified name"""
#     print(f"Hello, {name}!")



@app.cli.command("refresh_symbols")
def refresh_symbols():
    """
    To run use below command:
    flask -e config/dev.py -A manage.py refresh_symbols
    """

    try:
        Symbols.refresh_symbols()
    except Exception as e:
        print(str(e))
        raise e


@app.cli.command("get_stock_data")
@click.argument("time_range")
def get_stock_data(time_range="Historical"):
    """
    To run use below command:
    flask -e config/dev.py -A manage.py get_stock_data
    """

    try:
        print(StockPrice.fetch_stock_data())
    except Exception as e:
        print(str(e))
        raise e

