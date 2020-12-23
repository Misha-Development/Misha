import os
import json

import discord
from discord.ext import commands

from bot.utils.colors import Colors

class MishaBot(commands.Bot):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = json.load(open('bot/resources/messages.json', 'r'))
        self.load_cogs()

    async def on_ready(self):
        await self.change_presence(activity=discord.Game(name='Prefix: -m | Mishabot.org'))

    async def on_command_error(self, ctx, error):
        await ctx.channel.send(embed=discord.Embed(title='Invalid Command/Error Occured',
                                                   description=self.data['error'].replace('{prefix}', f'{self.command_prefix}'),
                                                   color=discord.Colour.red()))

    def load_cogs(self):
        print('Loading Extensions (cogs)')
        self.scan_directory('bot/exts')

    def scan_directory(self, dirName):
        for entry in os.listdir(dirName):
            path = f"{dirName}/{entry}"
            if os.path.isdir(path):
                self.scan_directory(path)
            else:
                if entry.endswith('.py'):
                    self.load_extension(f"{dirName.replace('/', '.')}.{entry[:-3]}")
