import os
import multiprocessing

from irc_bot import IRCBot
from discord_bot import DiscordBot
from assets.logo import display_logo

display_logo("3.0.1")


# create functions that define an instance of the bots and runs them
def start_irc_bot():
  irc_bot = IRCBot(
      server_list=[('irc.libera.chat', 6667)],
      nickname=os.environ['IRC_NICK'],
      realname=os.environ['IRC_NICK'],
      ident_password=os.environ['IRC_PASS'],
      channels=[
          os.environ['IRC_MOD_CHANNEL'], os.environ['IRC_WARNINGS_CHANNEL']
      ],
  )
  irc_bot.start()


def start_discord_bot():
  discord_bot = DiscordBot()
  try:
    discord_bot.run(os.environ['DISCORD_BOT_SECRET'])
  except Exception as e:
    print(f"DISCORD BOT ERROR: {e}")


# use multiprocessing to run both scripts concurrently
irc_process = multiprocessing.Process(target=start_irc_bot)
discord_process = multiprocessing.Process(target=start_discord_bot)

if __name__ == '__main__':
  irc_process.start()
  discord_process.start()
