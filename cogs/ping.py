import disnake
from disnake.ext import commands

class PingCommand(commands.Cog):
    """Ping command"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.slash_command(name="ping",description="Get the bots latency.")
    @commands.cooldown(rate= 1, per= 10, type= commands.BucketType.member)
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        """Get the bot's current websocket latency."""
        await inter.response.send_message(f"Pong! `Latency {round(self.bot.latency * 1000)}ms`")

def setup(bot: commands.Bot):
    bot.add_cog(PingCommand(bot))