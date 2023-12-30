import sqlite3


def check_player_exists(player):
  with sqlite3.connect("mod_db.sqlite") as conn:
    cur = conn.cursor()
    cur.execute(f"SELECT 1 FROM logs WHERE player = '{player}'")
    result = cur.fetchone()
  return result is not None


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


def debug():
  with sqlite3.connect("mod_db.sqlite") as conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM logs")
    rows = cur.fetchall()
    return rows


def update_action_taken(player, increment):
  with sqlite3.connect("mod_db.sqlite") as conn:
    cur = conn.cursor()

    if check_player_exists(player) is False:
      insert_query = """INSERT INTO logs (
        player, action_taken, tempbans, perma_banned
      ) VALUES (?, ?, ?, ?)"""
      cur.execute(insert_query, (
          player,
          increment,
          0,
          0,
      ))
      cur.execute(f"SELECT * FROM logs WHERE player = '{player}'")
      return cur.fetchone()

    cur.execute(
        f"UPDATE logs SET action_taken = action_taken + {increment} WHERE player = '{player}'"
    )
    cur.execute(f"SELECT * FROM logs WHERE player = '{player}'")
    return cur.fetchone()


def tempban(player):
  with sqlite3.connect("mod_db.sqlite") as conn:
    cur = conn.cursor()

    if check_player_exists(player) is False:
      insert_query = """INSERT INTO logs (
        player, action_taken, tempbans, perma_banned
      ) VALUES (?, ?, ?, ?)"""
      cur.execute(insert_query, (
          player,
          0,
          0,
          0,
      ))

    cur.execute(
        f"UPDATE logs SET tempbans = tempbans + 1 WHERE player = '{player}'")
    cur.execute(f"SELECT * FROM logs WHERE player = '{player}'")
    return cur.fetchone()


def ban(player):
  with sqlite3.connect("mod_db.sqlite") as conn:
    cur = conn.cursor()

    if check_player_exists(player) is False:
      insert_query = """INSERT INTO logs (
        player, action_taken, tempbans, perma_banned
      ) VALUES (?, ?, ?, ?)"""
      cur.execute(insert_query, (
          player,
          0,
          0,
          0,
      ))

    cur.execute(
        f"UPDATE logs SET perma_banned = perma_banned + 1 WHERE player = '{player}'")
    cur.execute(f"SELECT * FROM logs WHERE player = '{player}'")
    return cur.fetchone()
