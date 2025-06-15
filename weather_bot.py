import os
import logging
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
OPENWEATHER_TOKEN = os.environ.get("OPENWEATHER_TOKEN")

if TELEGRAM_TOKEN is None:
    raise RuntimeError("TELEGRAM_TOKEN environment variable not set")
if OPENWEATHER_TOKEN is None:
    raise RuntimeError("OPENWEATHER_TOKEN environment variable not set")

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Hello! Send /weather <city> to get the current weather."
    )

def weather(update: Update, context: CallbackContext) -> None:
    if not context.args:
        update.message.reply_text("Usage: /weather <city>")
        return
    city = " ".join(context.args)
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_TOKEN}&units=metric"
    )
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        update.message.reply_text(f"Weather in {city}: {temp}°C, {description}")
    except Exception as e:
        logger.error("Failed to fetch weather", exc_info=e)
        update.message.reply_text("Could not fetch weather data. Please try again.")

def main() -> None:
    updater = Updater(token=TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("weather", weather))

    updater.start_polling()
    logger.info("Bot started")
    updater.idle()

if __name__ == "__main__":
    main()
