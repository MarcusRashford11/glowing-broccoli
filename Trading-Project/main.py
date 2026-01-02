from src.load_data import load_yahoo_data
from src.returns import calculate_returns

df = load_yahoo_data("AAPL")
df = calculate_returns(df)

print(df[["Close", "returns"]].head(10))
print("shinooy")