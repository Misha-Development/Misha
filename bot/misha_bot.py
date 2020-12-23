import discord
from discord.ext import commands

class MishaBot(commands.Bot):

    def __init__(self, **kwargs):
        # Setting up prefix etc
        super().__init__(**kwargs)
        
        self.load_cogs()

    async def on_ready(self):
        await self.change_presence(activity=discord.Game(name='Prefix: -m | Mishabot.org'))

    async def on_command_error(self, ctx, error):
        await ctx.send(embed=discord.Embed(title='Invalid Command'))

    def load_cogs(self):
        print('Loading Extensions (cogs)')
        MishaBot.scan_directory('exts')

    @staticmethod
    def scan_directory(dirName):
        for entry in os.listdir(dirName):
            path = f"{dirName}/{entry}"
            if os.path.isdir(path):
                MishaBot.scan_directory(path)
            else:
                if entry.endswith('.py'):
                    self.load_extension(f"{dirName.replace('/', '.')}.{entry[:-3]}")
