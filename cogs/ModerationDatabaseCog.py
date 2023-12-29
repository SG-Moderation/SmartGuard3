from discord.ext import commands
from . import db


class ModerationDatabaseCog(commands.Cog):

  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.hybrid_command(name="create", description="Idk")
  async def cog1(self, ctx: commands.Context):
    db.create_database()
    await ctx.send("Done")

  @commands.hybrid_command(name="debug", description="Idk")
  async def cog1(self, ctx: commands.Context):
    db.debug()
    await ctx.send("Done")


async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(ModerationDatabaseCog(bot))
