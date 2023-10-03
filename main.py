import disnake
import os
import embed

from dotenv import load_dotenv
from disnake.ext import commands

load_dotenv()

bot = commands.InteractionBot(test_guilds=[1158529104384098426])

@bot.event
async def on_ready():
    print("The bot is ready!")
    print(f"Logged in as {bot.user} in {len(bot.guilds)} guilds")

bot.load_extensions("cogs/")
bot.run(os.getenv("DISCORD_TOKEN"))