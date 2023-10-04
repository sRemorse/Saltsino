import disnake
import os
import embeds

from dotenv import load_dotenv
from disnake.ext import commands

load_dotenv()

bot = commands.InteractionBot(
    test_guilds=[1158529104384098426],
    activity=disnake.Game(name=os.getenv("STATUS"))
    )

@bot.event
async def on_ready():
    print("The bot is ready!")
    print(f"Logged in as {bot.user} in {len(bot.guilds)} guilds")
    print(f"Status: {bot.status}")
    print(f"Activity: {bot.activity}")

# Global cooldown handler
@bot.event
async def on_slash_command_error(inter, error):
    if isinstance(error, commands.CommandOnCooldown):
        await inter.response.send_message(embed=embeds.createCooldownEmbed(round(error.retry_after)), ephemeral=True, delete_after=error.retry_after)

bot.load_extensions("cogs/")
bot.run(os.getenv("DISCORD_TOKEN"))