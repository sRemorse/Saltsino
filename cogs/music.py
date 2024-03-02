import os

import mafic
import disnake
from disnake.ext import commands
from config import lavalinkpass

class MusicCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.loop = bot.loop
        self.pool = mafic.NodePool(self.bot)
        try:
            self.loop.create_task(self.add_nodes())
        except Exception as e:
            print(f"Error connecting to Lavalink: {e}")

    async def add_nodes(self):
        try:
            await self.pool.create_node(
                host="127.0.0.1",
                port=2333,
                label="MAIN",
                password="lavalinkpass",
            )
        except Exception as e:
            print(f"Error creating Lavalink node: {e}")

    @commands.slash_command(name="play", dm_permission=False)
    async def play(self, inter, query: str):
        vc = inter.guild.voice_client

        if not vc:
            try:
                vc = await inter.author.voice.channel.connect(cls=mafic.Player)
            except disnake.ClientException:
                await inter.send("You must be in a voice channel to use this command.")
                return

        try:
            tracks = await vc.fetch_tracks(query)
        except mafic.errors.NoNodesAvailable:
            await inter.send("No Lavalink nodes available.")
            return

        if not tracks:
            await inter.send("No tracks found.")
            return

        track = tracks[0]

        try:
            await vc.play(track)
        except mafic.errors.NoNodesAvailable:
            await inter.send("No Lavalink nodes available to play track.")
            return

        await inter.send(f"Playing {track.title}.")

    @commands.slash_command(name='stop', description='Stop playing the current track.')
    async def stop(self, inter):
        if not inter.guild.voice_client or not inter.guild.voice_client.is_connected():
            return await inter.response.send_message("Not connected to a voice channel.")

        player = inter.guild.voice_client

        if isinstance(player, mafic.Player):
            try:
                if player.is_playing():
                    player.stop()
                    await inter.response.send_message("Stopped playing the current track.")
                else:
                    await inter.response.send_message("Not currently playing any music.")
            except AttributeError:
                # Handle AttributeError if player.is_playing() fails
                await inter.response.send_message("Failed to stop music: Invalid player object.")
        else:
            await inter.response.send_message("Invalid player object.")

    # @commands.slash_command(name="stop", dm_permission=False)
    # async def stop(self, inter):
    #     vc = inter.guild.voice_client

    #     if not vc or not vc.is_connected():
    #         await vc.stop()
    #         await inter.send("No music is currently playing.")
    #         return

    #     await vc.stop()
    #     await inter.send("Music stopped.")





def setup(bot):
    bot.add_cog(MusicCog(bot))
