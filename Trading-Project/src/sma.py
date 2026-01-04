def calculate_sma(df, price_col="Close", window=5):
    """
      Calculate a Simple Moving Average (SMA) for a given column.

      Parameters
      ----------
        df : pandas.DataFrame
          DataFrame containing the data.
        col : str, default "Close"
          The column name to calculate SMA on.
        window : int, default 5
          The number of periods for the SMA.

      Returns
      -------
        pandas.DataFrame
          A copy of the original DataFrame with a new column added:
          '<col>_sma<window>'
      """

    if price_col not in df.columns:
        raise ValueError(f"Column '{price_col}' not found in DataFrame")

    df = df.copy()
    df[f"{price_col}_sma{window}"] = df[price_col].rolling(window=window).mean()
    return df
