import disnake
from disnake.ext import commands
import embedManager as embeds

class UtilityCog(commands.Cog):
    """Utility Cog"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    # Ping command
    @commands.slash_command(name="ping",description="Get the bots latency.")
    @commands.cooldown(rate= 1, per= 10, type= commands.BucketType.member)
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        """Get the bot's current websocket latency."""
        await inter.response.send_message(embed=embeds.createEmbed(f"🏓 Pong!",f"Latency is {round(self.bot.latency * 1000)}ms"))
    
    # Server info command
    @commands.slash_command(name="serverinfo",description="Get this servers info.")
    @commands.cooldown(rate= 1, per= 10)
    async def serverinfo(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(embed=embeds.createEmbed(
            "💾 Server Info",
            f'Server name: {inter.guild.name}\nTotal members: {inter.guild.member_count}\nCreated on: {inter.guild.created_at.strftime("%d-%m-%Y")}')  
    )        

def setup(bot: commands.Bot):
    bot.add_cog(UtilityCog(bot))