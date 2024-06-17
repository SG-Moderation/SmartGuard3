from discord.ext import commands
from . import db

class ModerationDatabaseCog(commands.Cog):

  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.hybrid_command(
      name="create",
      description="Create the database for storing the moderation info.")
  async def create(self, ctx: commands.Context):
    print("[LOGS] Command !create has been run.")
    await ctx.send(db.create_database())

  @commands.hybrid_command(name="retrieve",
                           description="Retrieve the logs for a playe.r")
  async def retrieve(self, ctx: commands.Context, player):
    print("[LOGS] Command !retrieve has been run.")
    await ctx.send(db.retrieve(player))

  @commands.hybrid_command(name="delete",
                           description="Delete the database file.")
  async def delete(self, ctx: commands.Context):
    print("[LOGS] Command !delete has been run.")
    await ctx.send(db.delete_database())


  @commands.hybrid_command(
      name="warn",
      description="Update the warnings log for a player with an increment.")
  async def warn(self, ctx: commands.Context, player, increment: int):
    print("[LOGS] Command !warn has been run.")
    await ctx.send(db.warn(player, increment))

  @warn.error
  async def warn_error(self, ctx: commands.Context, error):
    if isinstance(error, commands.BadArgument):
      await ctx.send(
          "Invalid argument for increment. Please use postive integers only.")

  @commands.hybrid_command(name="tempban", description="Temp-ban a player.")
  async def tempban(self, ctx: commands.Context, player):
    print("[LOGS] Command !tempban has been run.")
    await ctx.send(db.tempban(player))

  @commands.hybrid_command(name="ban", description="Ban a player.")
  async def ban(self, ctx: commands.Context, player):
    print("[LOGS] Command !ban has been run.")
    await ctx.send(db.ban(player))

  @commands.hybrid_command(name="unban", description="Unban a player.")
  async def unban(self, ctx: commands.Context, player):
    print("[LOGS] Command !unban has been run.")
    await ctx.send(db.unban(player))


async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(ModerationDatabaseCog(bot))
