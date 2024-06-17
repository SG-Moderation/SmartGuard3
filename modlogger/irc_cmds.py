from . import db


class IrcCmds:

  def __init__(self, irc_channel):
    self.channel = irc_channel

  def listen(self, irc_connection, message):
    if message.startswith("!create"):
      print("[LOGS] Command !create has been run.")
      irc_connection.privmsg(self.channel, db.create_database())

    if message.startswith("!retrieve"):
      print("[LOGS] Command !retrieve has been run.")
      command_table = message.split()
      if len(command_table) > 1:
        irc_connection.privmsg(self.channel, db.retrieve(command_table[1]))
      else:
        irc_connection.privmsg(self.channel, "Invalid command usage")

    if message.startswith("!delete"):
      print("[LOGS] Command !delete has been run.")
      irc_connection.privmsg(self.channel, db.delete_database())

    if message.startswith("!warn"):
      print("[LOGS] Command !warn has been run.")
      command_table = message.split()
      if len(command_table) > 2:
        irc_connection.privmsg(self.channel,
                               db.warn(command_table[1], command_table[2]))
      else:
        irc_connection.privmsg(self.channel, "Invalid command usage")

    if message.startswith("!tempban"):
      print("[LOGS] Command !tempban has been run.")
      command_table = message.split()
      if len(command_table) > 1:
        irc_connection.privmsg(self.channel, db.tempban(command_table[1]))
      else:
        irc_connection.privmsg(self.channel, "Invalid command usage")

    if message.startswith("!ban"):
      print("[LOGS] Command !ban has been run.")
      command_table = message.split()
      if len(command_table) > 1:
        irc_connection.privmsg(self.channel, db.ban(command_table[1]))
      else:
        irc_connection.privmsg(self.channel, "Invalid command usage")

    if message.startswith("!unban"):
      print("[LOGS] Command !unban has been run.")
      command_table = message.split()
      if len(command_table) > 1:
        irc_connection.privmsg(self.channel, db.unban(command_table[1]))
      else:
        irc_connection.privmsg(self.channel, "Invalid command usage")
