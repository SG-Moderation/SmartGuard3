import os
import requests

import ib3.auth
import irc.bot

NICKNAME = os.environ['NICKNAME']
PASSWORD = os.environ['PASSWORD']
CHANNELS = [os.environ['CHANNEL']]

WEBHOOK = os.environ['WEBHOOK']


class IRCBot(ib3.auth.SASL, irc.bot.SingleServerIRCBot):

  def on_all_raw_messages(self, connection, event):
    print(event.arguments)

  def on_pubmsg(self, connection, event):
    # print(f"Message: {event.arguments[0]}, From: {event.source.nick}")
    data = {"content": event.arguments[0]}
    response = requests.post(WEBHOOK, json=data)


bot = IRCBot(
    server_list=[('irc.libera.chat', 6667)],
    nickname=NICKNAME,
    realname=NICKNAME,
    ident_password=PASSWORD,
    channels=CHANNELS,
)
bot.start()
