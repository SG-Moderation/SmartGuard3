import threading
import time


class SpamGuard:

  def __init__(self):
    self.check_spam_table = {}
    # start the periotic delete loop and run it alongside using threading
    threading.Thread(target=self.periotic_delete, daemon=True).start()

  # logs the message and the author to the check_spam_table
  # if there are too many messages logged into there, return true
  def is_spam(self, message, name):
    if name not in self.check_spam_table:
      self.check_spam_table[name] = []

    self.check_spam_table[name].append(message)

    if len(self.check_spam_table[name]) > 2:
      self.check_spam_table[name] = []
      return True

  # deletes the first message in the table every once in a while
  def periotic_delete(self):
    while True:
      time.sleep(4)
      for name in list(self.check_spam_table.keys()):
        if self.check_spam_table[name] and self.check_spam_table[name] != {}:
          self.check_spam_table[name].pop(0)
