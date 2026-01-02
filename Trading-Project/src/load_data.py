import yfinance as yf

def load_yahoo_data(symbol, start="2020-01-01", end=None):
    df = yf.download(symbol, start=start, end=end)

    # Flatten MultiIndex columns if present
    if isinstance(df.columns, tuple) or hasattr(df.columns, "levels"):
        df.columns = df.columns.get_level_values(0)

    return df
