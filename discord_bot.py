import discord
from discord.ext import commands

class DiscordBot(commands.Bot):

  def __init__(self):
    intents = discord.Intents.default()
    intents.message_content = True
    super().__init__(command_prefix="!", intents=intents)
    self.cogslist = ["modlogger.discord_cmds"]

  async def setup_hook(self):
    for ext in self.cogslist:
      await self.load_extension(ext)

  async def on_ready(self):
    print('We have logged in as {0.user}'.format(self))
    await self.tree.sync()
