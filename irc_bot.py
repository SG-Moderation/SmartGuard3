import os
import re
import requests

import ib3.auth
import irc.bot

from smartguard import SmartGuard
from blacklist import blacklist1, blacklist2


# removes color codings from the message
def strip_color_codes(message):
  pattern = re.compile(r"\x03(?:\d{1,2}(?:,\d{1,2})?)?|\x0f", re.UNICODE)
  return pattern.sub("", message)


class IRCBot(ib3.auth.SASL, irc.bot.SingleServerIRCBot):

  def __init__(self, *args, **kwargs):
    # inherit all properties and methods from its superclass
    super().__init__(*args, **kwargs)
    self.filter = SmartGuard()

  # print out all messages received from IRC
  def on_all_raw_messages(self, connection, event):
    print(event.arguments)

  # on all messages sent in public channels
  def on_pubmsg(self, connection, event):
    # use event.arguments[0] for message content
    # use  event.source.nick for message author

    # remove the CHANNEL_2 from the if statement unless for testing
    if event.target == os.environ['CHANNEL1'] or event.target == os.environ[
        'CHANNEL2']:
      message_original = strip_color_codes(event.arguments[0])

      # relay the chat to the relay discord channel
      data = {"content": message_original}
      response = requests.post(os.environ['RELAY_WEBHOOK'], json=data)

      # first word of the message is taken as the player the sent it
      # the rest of the message is taken as the message itself
      msg_org = message_original.split(maxsplit=1)
      msg_auth = msg_org[0]
      msg_cont = msg_org[1] if len(msg_org) > 1 else ""

      # run the message through the SmartGuard filters
      if self.filter.automod_check_a1(
          msg_cont, msg_auth, blacklist1) or self.filter.automod_check_a2(
              msg_cont, msg_auth, blacklist1) or self.filter.automod_check_b1(
                  msg_cont, msg_auth,
                  blacklist2) or self.filter.automod_check_b2(
                      msg_cont, msg_auth,
                      blacklist2) or self.filter.automod_check_b3(
                          msg_cont, msg_auth, blacklist2):
        # if the message contains swear, create a log
        log_message = f'Player {msg_auth} said "{msg_cont}"'

        # send the log to the logs Discord channel
        data = {"content": log_message}
        response = requests.post(os.environ['LOG_WEBHOOK'], json=data)

        # send the log to the logs IRC channel
        connection.privmsg(os.environ['CHANNEL2'], log_message)
