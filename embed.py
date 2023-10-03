import datetime
import disnake
    
def createCooldownEmbed(time):
    embed = disnake.Embed(title="Comand cooldown 🧊",
    description=f'Please try again in {time}s',
    color=disnake.Colour.blue(),
    timestamp=datetime.datetime.now(),
    )
    return embed


def createErrorEmbed(desc):
    embed = disnake.Embed(title="Error occured ❌",
    description=desc,
    color=disnake.Colour.red(),
    timestamp=datetime.datetime.now(),
    )
    return embed
    