from src.load_data import load_yahoo_data
from src.returns import calculate_returns
import pandas as pd

ticker = input("Write a valid ticker: ").upper()

try:
    df = load_yahoo_data(ticker)
    returns = calculate_returns(df)
    print(returns.head())
except KeyError:
    print(f"{ticker} is not a valid ticker")


#123
print("yellow")