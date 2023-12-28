import discord
from discord.ext import commands


class DiscordBot(commands.Bot):

  def __init__(self):
    intents = discord.Intents.default()
    super().__init__(command_prefix="!", intents=intents, help_command=None)

  async def on_ready(self):
    print('We have logged in as {0.user}'.format(self))
