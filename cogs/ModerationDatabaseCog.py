from discord.ext import commands
from . import db
import os


class ModerationDatabaseCog(commands.Cog):

  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.hybrid_command(
      name="create",
      description="Create the database for storing the moderation info.")
  async def create(self, ctx: commands.Context):
    print("[LOGS] Command !create has been run.")
    db.create_database()
    await ctx.send("Database created if it does not exist.")

  @commands.hybrid_command(name="retrieve",
                           description="Retrieve the logs for a playe.r")
  async def retrieve(self, ctx: commands.Context, player):
    print("[LOGS] Command !retrieve has been run.")
    data = db.retrieve(player)
    if data is None:
      await ctx.send(f"No logs found for player `{player}`.")
    else:
      await ctx.send(
          f"`{data[1]}`: {data[2]} warning(s), {data[3]} tempban(s), and {db.is_banned(player)}."
      )

  @commands.hybrid_command(name="delete",
                           description="Delete the database file.")
  async def delete(self, ctx: commands.Context):
    print("[LOGS] Command !delete has been run.")
    os.system("rm -rf ~/SmartGuard3/mod_db.sqlite")
    print("[LOGS] Deleted the database file.")
    await ctx.send("Deleted the database file.")

  @commands.hybrid_command(
      name="warn",
      description="Update the warnings log for a player with an increment.")
  async def warn(self, ctx: commands.Context, player, increment: int):
    result = db.warn(player, increment)
    banned_or_not = db.is_banned(player)
    await ctx.send(
        f"Warnings value updated by {increment} for player `{player}`")
    await ctx.send(
        f"`{result[1]}`: {result[2]} warning(s), {result[3]} tempban(s), and {banned_or_not}."
    )

  @warn.error
  async def warn_error(self, ctx: commands.Context, error):
    if isinstance(error, commands.BadArgument):
      await ctx.send(
          "Invalid argument for increment. Please use postive integers only.")

  @commands.hybrid_command(name="tempban", description="Temp-ban a player.")
  async def tempban(self, ctx: commands.Context, player):
    print("[LOGS] Command !tempban has been run.")
    db.tempban(player)
    await ctx.send(f"Tempbanned `{player}`.")

  @commands.hybrid_command(name="ban", description="Ban a player.")
  async def ban(self, ctx: commands.Context, player):
    print("[LOGS] Command !ban has been run.")
    if db.is_banned(player) == "is banned":
      await ctx.send(f"Player `{player}` is already banned.")
    else:
      db.ban(player)
      await ctx.send(f"Banned `{player}`.")

  @commands.hybrid_command(name="uban", description="Unban a player.")
  async def unban(self, ctx: commands.Context, player):
    print("[LOGS] Command !unban has been run.")
    if db.is_banned(player) == "is not banned":
      await ctx.send(f"Player `{player}` is not banned.")
    else:
      db.unban(player)
      await ctx.send(f"Unbanned `{player}`.")


async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(ModerationDatabaseCog(bot))
