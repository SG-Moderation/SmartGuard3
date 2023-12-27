########################################################################################################################

import os
import re
import requests

import ib3.auth
import irc.bot

from smartguard import SmartGuard
from blacklist import blacklist1, blacklist2

########################################################################################################################


def strip_color_codes(message):
  pattern = re.compile(r"\x03(?:\d{1,2}(?:,\d{1,2})?)?|\x0f", re.UNICODE)
  return pattern.sub("", message)


########################################################################################################################


class IRCBot(ib3.auth.SASL, irc.bot.SingleServerIRCBot):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.filter = SmartGuard()

  def on_all_raw_messages(self, connection, event):
    print(event.arguments)

  def on_pubmsg(self, connection, event):
    # print(f"Message: {event.arguments[0]}, From: {event.source.nick}")
    message_original = strip_color_codes(event.arguments[0])

    # relay the chat to #ctf-server
    data = {"content": message_original}
    response = requests.post(os.environ['RELAY_WEBHOOK'], json=data)

    # divide up the message
    msg_org = message_original.split(maxsplit=1)
    msg_auth = msg_org[0]
    msg_cont = msg_org[1] if len(msg_org) > 1 else ""

    # run the message through the filter
    if self.filter.automod_check_a1(
        msg_cont, msg_auth, blacklist1) or self.filter.automod_check_a2(
            msg_cont, msg_auth, blacklist1) or self.filter.automod_check_b1(
                msg_cont, msg_auth,
                blacklist2) or self.filter.automod_check_b2(
                    msg_cont, msg_auth,
                    blacklist2) or self.filter.automod_check_b3(
                        msg_cont, msg_auth, blacklist2):
      # print(f'Player {msg_auth} said "{msg_cont}"')
      data = {"content": f'Player {msg_auth} said "{msg_cont}"'}
      response = requests.post(os.environ['LOG_WEBHOOK'], json=data)


########################################################################################################################
