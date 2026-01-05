def signal_calculate(df, price_col="Close", sma_col="Close_sma5"):
    """
    Generate a trading signal based on price vs SMA.

    Signal:
    - 1 if price > SMA
    - 0 otherwise
    """
    if price_col not in df.columns:
        raise ValueError(f"{price_col} not found in DataFrame")
    if sma_col not in df.columns:
        raise ValueError(f"{sma_col} not found in DataFrame")

    df = df.copy()
    df["signal"] = (df[price_col] > df[sma_col]).astype(int)

    return df
