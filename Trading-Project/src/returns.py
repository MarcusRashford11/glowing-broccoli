def calculate_returns(df, price_col="Close"):
    n=20 
    """
    Add a returns column based on percentage change.
    """
    if price_col not in df.columns:
        raise ValueError(f"Column '{price_col}' not found in DataFrame")

    df = df.copy()
    df["returns"] = df[price_col].pct_change()

    df["return_lag_1"]=df["returns"].shift(1)

    df["return_lag_7"]=df["returns"].shift(7)

    #if df["returns"].shift(n)>df["returns"].shift(n+1):
    #    df["positive"]= "+"
    #else:
    #    df["positive"]= "-"
    return df
