import datetime
import disnake

    
def createCooldownEmbed(time: float):
    """Creates ephmeral embed displaying the time left to re-use a command and deletes after the cooldown"""
    embed = disnake.Embed(title="Comand cooldown 🧊",
    description=f'Please try again in {time}s',
    color=disnake.Colour.gold(),
    timestamp=datetime.datetime.utcnow()
    )
    return embed


def createErrorEmbed(desc: str):
    """Creates ephmeral error embed with red colour"""
    embed = disnake.Embed(title="Error occured ❌",
    description=desc,
    color=disnake.Colour.red(),
    timestamp=datetime.datetime.now(),
    )
    return embed

def createEmbed(title: str, desc: str):
    """Creates a standard embed with light grey colour"""
    embed = disnake.Embed(title=title,
    description=desc,
    color=disnake.Colour.blue(),
    timestamp=datetime.datetime.now(),
    )
    return embed
    