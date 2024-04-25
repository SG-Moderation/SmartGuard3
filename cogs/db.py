import sqlite3
import os


def check_player_exists(player, cur):
  print(f"[LOGS] Checking if player {player} exists.")
  cur.execute("SELECT 1 FROM logs WHERE player = ?", (player, ))
  result = cur.fetchone()
  if result is None:
    insert_query = """INSERT INTO logs (
        player, action_taken, tempbans, perma_banned
      ) VALUES (?, ?, ?, ?)"""
    cur.execute(insert_query, (
        player,
        0,
        0,
        0,
    ))
    print(f"[LOGS] Player {player} added to database")
  else:
    print(f"[LOGS] Log for player {player} already exists in database.")


def create_database():
  with sqlite3.connect("mod_db.sqlite") as conn:
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS logs (
      id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
      player TEXT UNIQUE NOT NULL,
      action_taken INTEGER NOT NULL,
      tempbans INTEGER NOT NULL,
      perma_banned INTEGER
    )""")
    msg = "Database created if it does not exist."
    print(f"[LOGS] {msg}")
    return msg


def delete_database():
  print("[LOGS] Command !delete has been run.")
  os.system("rm -rf ~/SmartGuard3/mod_db.sqlite")
  print("[LOGS] Deleted the database file.")
  return "Deleted the database file."


def retrieve(player):
  with sqlite3.connect("mod_db.sqlite") as conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM logs WHERE player = ?", (player, ))
    data = cur.fetchone()
    print(f"[LOGS] Retrieved logs for player {player}.")
    if data is None:
      return f"No logs found for player `{player}`"
    else:
      return f"`{data[1]}`: {data[2]} warning(s), {data[3]} tempban(s), and {is_banned(player)}."


def warn(player, increment):
  with sqlite3.connect("mod_db.sqlite") as conn:
    cur = conn.cursor()

    check_player_exists(player, cur)

    cur.execute(
        """
        UPDATE logs SET action_taken = action_taken + ? WHERE player = ?
        """, (
            int(increment),
            player,
        ))
    conn.commit()
    msg1 = f"Warnings value updated by {increment} for player `{player}`."
    print(f"[LOGS] {msg1}")

    return f"{msg1}  {retrieve(player)}"


def tempban(player):
  with sqlite3.connect("mod_db.sqlite") as conn:
    cur = conn.cursor()

    check_player_exists(player, cur)

    cur.execute("UPDATE logs SET tempbans = tempbans + 1 WHERE player = ?",
                (player, ))
    msg = f"Tempbanned `{player}`."
    print(f"[LOGS] {msg}")
    return msg


def ban(player):
  if is_banned(player) == "is banned":
    return f"Player `{player}` is already banned."
  else:
    with sqlite3.connect("mod_db.sqlite") as conn:
      cur = conn.cursor()

      check_player_exists(player, cur)

      cur.execute(
          f"UPDATE logs SET perma_banned = perma_banned + 1 WHERE player = '{player}'"
      )
      msg = f"Banned `{player}`."
      print(f"[LOGS] {msg}")
      return msg


def unban(player):
  if is_banned(player) == "is not banned":
    return f"Player `{player}` is not banned."
  else:
    with sqlite3.connect("mod_db.sqlite") as conn:
      cur = conn.cursor()

      check_player_exists(player, cur)

      cur.execute("UPDATE logs SET perma_banned = 0 WHERE player = ?",
                  (player, ))
      msg = f"Unbanned `{player}`."
      print(f"[LOGS] {msg}")
    return msg


def is_banned(player):
  with sqlite3.connect("mod_db.sqlite") as conn:
    cur = conn.cursor()
    cur.execute("""SELECT perma_banned FROM logs WHERE player = ?""",
                (player, ))
    if cur.fetchall()[0][0] == 0:
      str = "is not banned"
    else:
      str = "is banned"
    return str
