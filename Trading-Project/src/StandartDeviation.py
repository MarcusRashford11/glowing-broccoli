def calculate_std(df, price_col="close"):

    '''
    This function will calculate a STD within a given time period 

    STD = standart deviation.

    meaning the funcrion will decide if the "stock" is 
    risky or safe to handle whilst using the 
    returns to calculate the given risks

    '''
    if price_col not in df.columns:
        raise ValueError(f"Column '{price_col}' not found in DataFrame")
    
    df=df.copy()
    df["std20_col"]=df["returns"].rolling(window=20).std()

    return df 

