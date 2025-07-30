import os

API_KEY = os.getenv("OANDA_API_KEY")
ACCOUNT_ID = os.getenv("OANDA_ACCOUNT_ID")
OANDA_URL = "https://api-fxpractice.oanda.com/v3"

SECURE_HEADER = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

SELL = -1
BUY = 1
NONE = 0