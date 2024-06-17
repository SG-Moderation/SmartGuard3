import os
import re
import requests

import ib3.auth
import irc.bot

import smartguard
import modlogger


# removes color codings from the message
def strip_color_codes(message):
  pattern = re.compile(r"\x03(?:\d{1,2}(?:,\d{1,2})?)?|\x0f", re.UNICODE)
  return pattern.sub("", message)


class IRCBot(ib3.auth.SASL, irc.bot.SingleServerIRCBot):

  def __init__(self, *args, **kwargs):
    # inherit all properties and methods from its superclass
    super().__init__(*args, **kwargs)
    self.sus_check = smartguard.SmartGuard()
    self.spam_check = smartguard.SpamGuard()
    self.mdb_commands = modlogger.IrcCmds(os.environ['IRC_WARNINGS_CHANNEL'])

  # print out all messages received from IRC
  def on_all_raw_messages(self, connection, event):
    print(event.arguments[0])

  # on all messages sent in public channels
  def on_pubmsg(self, connection, event):
    # use event.arguments[0] for message content
    # use  event.source.nick for message author

    # listen to commands on specific channels
    if event.target == os.environ['IRC_WARNINGS_CHANNEL']:
      self.mdb_commands.listen(connection, event.arguments[0])

    # run the filter on specific channels
    # remove the CHANNEL_2 from the if statement unless for testing
    if event.target == os.environ['IRC_MOD_CHANNEL']:
      message_original = strip_color_codes(event.arguments[0])

      # relay the chat to the relay discord channel
      data = {"content": message_original}
      response = requests.post(os.environ['IRC_CHAT_RELAY_WEBHOOK'], json=data)

      # first word of the message is taken as the player the sent it
      # the rest of the message is taken as the message itself
      msg_org = message_original.split(maxsplit=1)
      msg_auth = msg_org[0]
      msg_cont = msg_org[1] if len(msg_org) > 1 else ""

      # run the message through SmartGuard's checks
      if self.sus_check.is_sus(msg_cont, msg_auth, smartguard.blacklist1, smartguard.blacklist2):
        # if the message contains swear, create a log
        log_message = f'Player {msg_auth} said "{msg_cont}"'

        # send the log to the logs Discord channel
        data = {"content": log_message}
        response = requests.post(os.environ['IRC_WARNINGS_RELAY_WEBHOOK'],
                                 json=data)

        # send the log to the logs IRC channel
        connection.privmsg(os.environ['IRC_WARNINGS_CHANNEL'], log_message)

      # run the message through SpamGuard's check
      if self.spam_check.is_spam(msg_cont, msg_auth):
        # if the message is spam, create a log
        spam_warning = f'Player {msg_auth} is sending messages too fast'

        # send the warning to the logs Discord channel
        data = {"content": spam_warning}
        response = requests.post(os.environ['IRC_WARNINGS_RELAY_WEBHOOK'],
                                 json=data)

        # send the warning to the logs IRC channel
        connection.privmsg(os.environ['IRC_WARNINGS_CHANNEL'], spam_warning)
