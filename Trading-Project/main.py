from src.load_data import load_yahoo_data
from src.returns import calculate_returns
from src.sma import calculate_sma
from src.signal import signal_calculate
from src.StandartDeviation import calculate_std
import pandas as pd

# Ask user for ticker
ticker = input("Enter a valid ticker: ").upper()

try:
    # 1. Load OHLCV data
    df = load_yahoo_data(ticker)
    
    # 2. Calculate daily returns
    df = calculate_returns(df)  # Adds 'returns' column

    # 3. Calculate 5-day SMA of **price**
    df = calculate_sma(df, price_col="Close")  # Column: 'sma5'

    # 4. Optional: calculate 5-day SMA of returns
    df = calculate_sma(df, price_col="returns")  # Column: 'returns_sma5'

    # 5. Show all rows and columns without truncation
    pd.set_option("display.max_rows", 10)
    pd.set_option("display.max_columns", 10)

    #6. calculate and give a signal based on SMA5 and closing prices 

    df = signal_calculate(df, price_col="Close", sma_col="Close_sma5")

    #7. gives a STD = standard deviation. wich gives an indicadition wethear the stock is "risky" or "safe"
    df = calculate_std(df,price_col="Close")
 
    # . Print the full DataFrame with selected columns
    print(df[["Close", "High", "Low", "Open", "Volume",
          "returns", "return_lag_1", "return_lag_7",
          "Close_sma5","signal","std20_col"]])

except Exception as e:
    print(f"Error with ticker '{ticker}': {e}")

print("Finished processing", ticker)
print(df.columns)