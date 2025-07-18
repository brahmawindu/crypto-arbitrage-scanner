import requests
import time

def fetch_binance_price(symbol="BTCUSDT"):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    try:
        res = requests.get(url)
        data = res.json()
        return float(data["price"])
    except:
        print("❌ Не удалось получить цену с Binance")
        return None

def fetch_coinbase_price(symbol="BTC-USD"):
    url = f"https://api.coinbase.com/v2/prices/{symbol}/spot"
    try:
        res = requests.get(url)
        data = res.json()
        return float(data["data"]["amount"])
    except:
        print("❌ Не удалось получить цену с Coinbase")
        return None

def check_arbitrage(symbol_binance="BTCUSDT", symbol_coinbase="BTC-USD"):
    price_binance = fetch_binance_price(symbol_binance)
    price_coinbase = fetch_coinbase_price(symbol_coinbase)

    if price_binance and price_coinbase:
        diff = price_coinbase - price_binance
        percent = (diff / price_binance) * 100

        print("\n📊 Цены:")
        print(f"🔹 Binance:  ${price_binance:.2f}")
        print(f"🔸 Coinbase: ${price_coinbase:.2f}")
        print(f"💱 Разница:  ${diff:.2f} ({percent:.2f}%)")

        if abs(percent) > 0.5:
            print("⚡ Возможность арбитража обнаружена!")
        else:
            print("ℹ️ Разница слишком мала для арбитража.")

if __name__ == "__main__":
    while True:
        check_arbitrage()
        time.sleep(30)  # Проверка каждые 30 секунд
