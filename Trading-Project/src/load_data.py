import yfinance as yf

def load_yahoo_data(symbol, start="2025-01-01", end=None):
   #download the data from yahoo finance 
    df = yf.download(symbol, start=start, end=end)

    # Flatten MultiIndex columns if present and if so, flattenes them. 
    if hasattr(df.columns, "levels"):
     df.columns = df.columns.get_level_values(0)

    return df
