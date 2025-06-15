# Weather Telegram Bot

This repository contains a simple Telegram bot that fetches current weather
information using the OpenWeather API.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set the following environment variables:
   - `TELEGRAM_TOKEN` – your Telegram bot token.
   - `OPENWEATHER_TOKEN` – your OpenWeather API key.
3. Run the bot:
   ```bash
   python weather_bot.py
   ```

Send `/weather <city>` to the bot to receive the current temperature and
weather description for that city.
