########################################################################################################################

import os
import requests
import re

import ib3.auth
import irc.bot

from smartguard import *
from blacklist1 import blacklist1
from blacklist2 import blacklist2
from keep_alive import keep_alive

########################################################################################################################

NICKNAME = os.environ['NICKNAME']
PASSWORD = os.environ['PASSWORD']
CHANNELS = [os.environ['CHANNEL1'], os.environ['CHANNEL2']]

RELAY_WEBHOOK = os.environ['RELAY_WEBHOOK']
LOG_WEBHOOK = os.environ['LOG_WEBHOOK']


def strip_color_codes(message):
  pattern = re.compile(r"\x03(?:\d{1,2}(?:,\d{1,2})?)?|\x0f", re.UNICODE)
  return pattern.sub("", message)


########################################################################################################################


class IRCBot(ib3.auth.SASL, irc.bot.SingleServerIRCBot):

  def on_all_raw_messages(self, connection, event):
    print(event.arguments)

  def on_pubmsg(self, connection, event):
    # print(f"Message: {event.arguments[0]}, From: {event.source.nick}")
    message_original = strip_color_codes(event.arguments[0])

    # relay the chat to #ctf-server
    data = {"content": message_original}
    response = requests.post(RELAY_WEBHOOK, json=data)

    # divide up the message
    msg_org = message_original.split(maxsplit=1)
    msg_auth = msg_org[0]
    msg_cont = msg_org[1]

    # run the message through the filter
    if automod_check_a1(msg_cont, msg_auth, blacklist1) or automod_check_a2(
        msg_cont, msg_auth, blacklist1) or automod_check_b1(
            msg_cont, msg_auth, blacklist2) or automod_check_b2(
                msg_cont, msg_auth, blacklist2) or automod_check_b3(
                    msg_cont, msg_auth, blacklist2):
      # print(f'Player {msg_auth} said "{msg_cont}"')
      data = {"content": f'Player {msg_auth} said "{msg_cont}"'}
      response = requests.post(LOG_WEBHOOK, json=data)


########################################################################################################################

bot = IRCBot(
    server_list=[('irc.libera.chat', 6667)],
    nickname=NICKNAME,
    realname=NICKNAME,
    ident_password=PASSWORD,
    channels=CHANNELS,
)
keep_alive()
bot.start()

########################################################################################################################
