import yfinance as yf

def get_financials(stock):
    ticker = yf.Ticker(stock)
    info = ticker.info

    return {
        "name": info.get("longName"),
        "sector": info.get("sector"),
        "marketCap": info.get("marketCap"),
        "pe": info.get("trailingPE"),
        "revenueGrowth": info.get("revenueGrowth"),
    }


def get_price_history(stock):
    ticker = yf.Ticker(stock)
    hist = ticker.history(period="1mo")

    return {
        "dates": hist.index.strftime("%Y-%m-%d").tolist(),
        "prices": hist["Close"].tolist()
    }
