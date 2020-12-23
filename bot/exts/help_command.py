import discord
from discord.ext import commands

class HelpCommand(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client


def setup(client):
    client.add_cog(HelpCommand(client))
