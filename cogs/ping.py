import disnake
from disnake.ext import commands
import embeds

class PingCommand(commands.Cog):
    """Ping command"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.slash_command(name="ping",description="Get the bots latency.")
    @commands.cooldown(rate= 1, per= 10)
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        """Get the bot's current websocket latency."""
        await inter.response.send_message(f"Pong! `Latency {round(self.bot.latency * 1000)}ms`")

    @ping.error
    async def cooldown_error(self, inter, error):
        
        if isinstance(error, commands.CommandOnCooldown):
            await inter.response.send_message(embed=embeds.createCooldownEmbed(round(error.retry_after)), ephemeral=True, delete_after=error.retry_after)

def setup(bot: commands.Bot):
    bot.add_cog(PingCommand(bot))