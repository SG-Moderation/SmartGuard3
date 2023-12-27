########################################################################################################################

import os

from irc_bot import IRCBot
from keep_alive import keep_alive

########################################################################################################################

bot = IRCBot(
    server_list=[('irc.libera.chat', 6667)],
    nickname=os.environ['NICKNAME'],
    realname=os.environ['NICKNAME'],
    ident_password=os.environ['PASSWORD'],
    channels=[os.environ['CHANNEL1']],
)

keep_alive()
bot.start()

########################################################################################################################
