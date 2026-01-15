import time
import requests
from datetime import datetime

PYTH_URL = "https://hermes.pyth.network/v2/updates/price/latest"
PYTH_FEED_ID = "0xe62df6c8b4a85fe1b4c7c0b6b1c8f1f1cbb18b19c9f7e2f3a3c1e9e6b3d8a9c4"  # ZEC/USD

def get_price():
    try:
        r = requests.get(
            PYTH_URL,
            params={"ids[]": PYTH_FEED_ID},
            timeout=10
        )
        data = r.json()

        price_info = data["parsed"][0]["price"]
        price = int(price_info["price"])
        expo = int(price_info["expo"])

        real_price = price * (10 ** expo)
        return real_price

    except Exception as e:
        print("Price error:", e)
        return None


print("🚀 Bot started")

while True:
    price = get_price()
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    if price:
        print(f"[{now}] ZEC price: {price}")
    else:
        print(f"[{now}] Waiting for price...")

    time.sleep(30)

