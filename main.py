import os
import time
import multiprocessing

from irc_bot import IRCBot
from discord_bot import DiscordBot
from assets.sg_logo import SGLogo

logo = SGLogo("3.3.0")
logo.display()


# create functions that define an instance of the bots and runs them
def start_irc_bot():
  while True:
    try:
      irc_bot = IRCBot(
          server_list=[(os.environ['IRC_SERVER'], int(os.environ['IRC_PORT']))],
          nickname=os.environ['IRC_NICK'],
          realname=os.environ['IRC_NICK'],
          ident_password=os.environ['IRC_PASS'],
          channels=[
              os.environ['IRC_MOD_CHANNEL'], os.environ['IRC_WARNINGS_CHANNEL']
          ],
      )
      irc_bot.start()
    # catch any exception
    except Exception as e:
      print(f"IRC BOT ERROR: {e}, RESTARTING IN 5 SECONDS...")
      time.sleep(5)


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
  if os.environ['ENABLE_DISCORD_BOT'] == "true":
    discord_process.start()
