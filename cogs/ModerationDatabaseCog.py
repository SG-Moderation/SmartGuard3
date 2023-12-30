from discord.ext import commands
from . import db
import os


class ModerationDatabaseCog(commands.Cog):

  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.hybrid_command(name="create", description="Idk")
  async def create(self, ctx: commands.Context):
    db.create_database()
    await ctx.send("Done")

  @commands.hybrid_command(name="debug", description="Idk")
  async def debug(self, ctx: commands.Context):
    rows = db.debug()
    for row in rows:
      await ctx.send(row)

  @commands.hybrid_command(name="delete", description="Idk")
  async def delete(self, ctx: commands.Context):
    os.system("rm -rf ~/SmartGuard3/mod_db.sqlite")
    await ctx.send("Deleted")

  @commands.hybrid_command(name="update", description="Idk")
  async def update(self, ctx: commands.Context, player, increment: int):
    result = db.update_action_taken(player, increment)
    await ctx.send(f"Updated: {result}")

  @update.error
  async def update_error(self, ctx: commands.Context, error):
    if isinstance(error, commands.BadArgument):
      await ctx.send("Invalid argument(s).")

  @commands.hybrid_command(name="tempban", description="Idk")
  async def tempban(self, ctx: commands.Context, player):
    result = db.tempban(player)
    await ctx.send(f"Tempbanned: {result}")

  @commands.hybrid_command(name="ban", description="Idk")
  async def ban(self, ctx: commands.Context, player):
    result = db.ban(player)
    await ctx.send(f"Banned: {result}")


async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(ModerationDatabaseCog(bot))
