def calculate_returns(df, price_col="Close"):
    """
    Add a returns column based on percentage change.
    """
    if price_col not in df.columns:
        raise ValueError(f"Column '{price_col}' not found in DataFrame")

    df = df.copy()
    df["returns"] = df[price_col].pct_change()

    df["return_lag_1"]=df["returns"].shift(1)

    df["return_lag_7"]=df["returns"].shift(7)
    return df
