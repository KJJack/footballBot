import discord
import os
from dotenv import load_dotenv
from DiscordBot import DiscordBot

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
bot = DiscordBot()
bot.run(TOKEN)
