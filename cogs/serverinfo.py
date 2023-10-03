import disnake
from disnake.ext import commands
import embeds

class ServerinfoCommand(commands.Cog):
    """Server info command"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.slash_command(name="serverinfo",description="Get this servers info.")
    @commands.cooldown(rate= 1, per= 10)
    async def serverinfo(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(
        f'Server name: {inter.guild.name}\nTotal members: {inter.guild.member_count}\nCreated on: {inter.guild.created_at.strftime("%d-%m-%Y")}'
    )
        
        
    @serverinfo.error
    async def cooldown_error(self, inter, error):
        if isinstance(error, commands.CommandOnCooldown):
            await inter.response.send_message(embed=embeds.createCooldownEmbed(round(error.retry_after)), ephemeral=True, delete_after=error.retry_after)

def setup(bot: commands.Bot):
    bot.add_cog(ServerinfoCommand(bot))