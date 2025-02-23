# bot_token.py
# ~~~ read the discord bot token ~~~
# To get the token:
# Go the Discord Developer Portal => select your bot
# Click on "Reset Token" to generate a new one, use that.

import os
import sys
import configparser

# set `prefer_env` to `True` if you wish to prioritize the environment variable over the configuration text file
# (determines load order)
def get_discord_bot_token():
    config = configparser.ConfigParser()
    config.read('config.ini')
    prefer_env = config.getboolean('DEFAULT', 'PreferEnvForBotToken', fallback=True)

    if prefer_env:
        bot_token = os.getenv('DISCORD_BOT_TOKEN')
        if bot_token is not None:
            return bot_token

    try:
        with open('discord_bot_token.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        if not prefer_env:
            bot_token = os.getenv('DISCORD_BOT_TOKEN')
            if bot_token is not None:
                return bot_token

        print("The DISCORD_BOT_TOKEN environment variable is not set, and `discord_bot_token.txt` was not found. Please set either one and adjust `config.ini` if needed for the preferred load order.")
        sys.exit(1)