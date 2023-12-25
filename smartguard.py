########################################################################################################################


# function that removes duplicated characters
def remove_duplicates(s):
  return ''.join(dict.fromkeys(s))


# function that removes spaces
def remove_spaces(s):
  no_space = s.replace(" ", "")
  return no_space


# function that only keeps letters
def remove_all(s):
  all_removed = ''.join(c for c in s if c.isalpha())
  return all_removed


# function that only keeps letters and spaces
def remove_parts(s):
  parts_removed = ''.join(c for c in s if c.isalpha() or c.isspace())
  return parts_removed


# function that replaces special character with spaces
def replace_parts(s):
  parts_removed = ''.join(c if c.isalpha() or c.isspace() else ' ' for c in s)
  return parts_removed


########################################################################################################################

# define
last_messages_a1 = {}
last_messages_a2 = {}
last_messages_b1 = {}
last_messages_b2 = {}
last_messages_b3 = {}
last_messages_wl = {}


# removes all special characters, spaces so it is just pure plain text
# first if tests with duplicates, second if without
def automod_check_a1(message, name, blacklist):
  if name not in last_messages_a1:
    last_messages_a1[name] = []

  message = remove_all(message.lower())
  last_messages_a1[name].append(message)

  if len(last_messages_a1[name]) > 20:
    last_messages_a1[name].pop(0)

  last_messages_str_a1 = ''.join(last_messages_a1[name])
  for word in blacklist:
    if word in last_messages_str_a1:
      last_messages_a1[name] = []
      return True
    elif word in remove_duplicates(last_messages_str_a1):
      last_messages_a1[name] = []
      return True


# removes all spaces but keep special characters
# first if tests with duplicates, second if without
def automod_check_a2(message, name, blacklist):
  if name not in last_messages_a2:
    last_messages_a2[name] = []

  message = remove_spaces(message.lower())
  last_messages_a2[name].append(message)

  if len(last_messages_a2[name]) > 20:
    last_messages_a2[name].pop(0)

  last_messages_str_a2 = ''.join(last_messages_a2[name])
  for word in blacklist:
    if word in last_messages_str_a2:
      last_messages_a2[name] = []
      return True
    elif word in remove_duplicates(last_messages_str_a2):
      last_messages_a2[name] = []
      return True


# removes all special characters but keep spaces
# a space is added at the end of each message in the table
# first if tests with duplicates, second if without
def automod_check_b1(message, name, blacklist):
  if name not in last_messages_b1:
    last_messages_b1[name] = []

  message = (remove_parts(message.lower()) + " ")
  last_messages_b1[name].append(message)

  if len(last_messages_b1[name]) > 20:
    last_messages_b1[name].pop(0)

  last_messages_str_b1 = ''.join(last_messages_b1[name])
  for word in blacklist:
    if word in last_messages_str_b1:
      last_messages_b1[name] = []
      return True
    elif word in remove_duplicates(last_messages_str_b1):
      last_messages_b1[name] = []
      return True


# replace all special characters with spaces
# a space is added at the end of each message in the table
# first if tests with duplicates, second if without
def automod_check_b2(message, name, blacklist):
  if name not in last_messages_b2:
    last_messages_b2[name] = []

  message = (replace_parts(message.lower()) + " ")
  last_messages_b2[name].append(message)

  if len(last_messages_b2[name]) > 20:
    last_messages_b2[name].pop(0)

  last_messages_str_b2 = ''.join(last_messages_b2[name])
  for word in blacklist:
    if word in last_messages_str_b2:
      last_messages_b2[name] = []
      return True
    elif word in remove_duplicates(last_messages_str_b2):
      last_messages_b2[name] = []
      return True


# keep special characters and spaces but remove duplicates
# a space is added at the end of each message in the table
def automod_check_b3(message, name, blacklist):
  if name not in last_messages_b3:
    last_messages_b3[name] = []

  message = (remove_duplicates(message.lower()) + " ")
  last_messages_b3[name].append(message)

  if len(last_messages_b3[name]) > 20:
    last_messages_b3[name].pop(0)

  last_messages_str_b3 = ''.join(last_messages_b3[name])
  for word in blacklist:
    if word in last_messages_str_b3:
      last_messages_b3[name] = []
      return True


########################################################################################################################
