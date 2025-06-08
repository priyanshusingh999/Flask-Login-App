import requests, time
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

# Telegram bot token and chat ID placeholders - replace with your actual values
TELEGRAM_BOT_TOKEN = f"{TELEGRAM_BOT_TOKEN}"
TELEGRAM_CHAT_ID = f"{TELEGRAM_CHAT_ID}"

def send_telegram_message(name, email, message, msg_time):
    text = f"<b>Contact Form Submission</b>\n\nName: {name}\n\nEmail: {email}\n\nMessage: {message}\n\nTime: {msg_time}"
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text, "parse_mode": "HTML"}
    try:
        resp = requests.post(url, data=payload, timeout=10)
        if resp.status_code != 200:
            print(f"Failed to send Telegram message: {resp.text}")
            return False
    except Exception as e:
        print(f"Exception while sending Telegram message: {e}")
        return False
    return True