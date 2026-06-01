import yfinance as yf

def get_signal(symbol):
    data = yf.download(symbol, period="3mo")
    close = data["Close"]

    ma20 = close.rolling(20).mean()

    price = close.iloc[-1]
    ma = ma20.iloc[-1]

    if price > ma:
        return "BUY", "70%"
    elif price < ma:
        return "SELL", "20%"
    else:
        return "HOLD", "40%"
