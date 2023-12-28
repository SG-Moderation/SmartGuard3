########################################################################################################################

import os
import multiprocessing

from irc_bot import IRCBot
from discord_bot import DiscordBot
from keep_alive import keep_alive

########################################################################################################################


def start_irc_bot():
  irc_bot = IRCBot(
      server_list=[('irc.libera.chat', 6667)],
      nickname=os.environ['NICKNAME'],
      realname=os.environ['NICKNAME'],
      ident_password=os.environ['PASSWORD'],
      channels=[os.environ['CHANNEL1'], os.environ['CHANNEL2']],
  )
  irc_bot.start()


def start_discord_bot():
  discord_bot = DiscordBot()
  discord_bot.run(os.getenv("DISCORD_BOT_SECRET"))


keep_alive()

irc_process = multiprocessing.Process(target=start_irc_bot)
discord_process = multiprocessing.Process(target=start_discord_bot)

irc_process.start()
discord_process.start()

########################################################################################################################
