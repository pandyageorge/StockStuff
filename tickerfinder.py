import yfinance as yf
from yahoo_fin.stock_info import tickers_nasdaq as get_nasdaq_tickers

# This method pulls an exhaustive list of stocks within a certain market cap
def get_tickers_by_market_cap(min_cap, max_cap):
    # Fetch all NASDAQ tickers. This should cover a significant portion of US-listed stocks.
    all_tickers = get_nasdaq_tickers()
    selected_tickers = []

    for ticker in all_tickers:
        try:
            stock = yf.Ticker(ticker)
            market_cap = stock.info["marketCap"]
            
            if min_cap <= market_cap <= max_cap:
                selected_tickers.append(ticker)

        except Exception as e:
            print(f"Could not fetch data for {ticker} due to {e}")

    return selected_tickers

def main():
    min_market_cap = 100e6  # e.g., 100 million
    max_market_cap = 50e9  # e.g., 50 billion

    tickers = get_tickers_by_market_cap(min_market_cap, max_market_cap)

    # Write tickers to a txt file
    with open("filtered_tickers.txt", "w") as f:
        for ticker in tickers:
            f.write(f"{ticker}\n")

    print(f"{len(tickers)} tickers written to filtered_tickers.txt")
    
if __name__ == "__main__":
    main()