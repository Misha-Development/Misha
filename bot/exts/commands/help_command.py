import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        await ctx.channel.send('Testing')

def setup(client):
    client.add_cog(Help(client))
