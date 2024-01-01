import sqlite3


def check_player_exists(player, cur):
  print(f"[LOGS] Checking if player {player} exists,")
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
    print("[LOGS] Database created if it does not exist.")


def retrieve(player):
  with sqlite3.connect("mod_db.sqlite") as conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM logs WHERE player = ?", (player, ))
    data = cur.fetchone()
    print(f"[LOGS] Retrieved logs for player {player}.")
    return data


def warn(player, increment):
  with sqlite3.connect("mod_db.sqlite") as conn:
    cur = conn.cursor()

    check_player_exists(player, cur)

    cur.execute(
        """
        UPDATE logs SET action_taken = action_taken + ? WHERE player = ?
        """, (
            increment,
            player,
        ))
    print(f"[LOGS] Warnings value updated by {increment} for {player}.")
    cur.execute("SELECT * FROM logs WHERE player = ?", (player, ))
    return cur.fetchone()


def tempban(player):
  with sqlite3.connect("mod_db.sqlite") as conn:
    cur = conn.cursor()

    check_player_exists(player, cur)

    cur.execute("UPDATE logs SET tempbans = tempbans + 1 WHERE player = ?",
                (player, ))
    print(f"[LOGS] Tempbanned {player}.")


def ban(player):
  with sqlite3.connect("mod_db.sqlite") as conn:
    cur = conn.cursor()

    check_player_exists(player, cur)

    cur.execute(
        f"UPDATE logs SET perma_banned = perma_banned + 1 WHERE player = '{player}'"
    )
    print(f"[LOGS] Banned {player}.")


def unban(player):
  with sqlite3.connect("mod_db.sqlite") as conn:
    cur = conn.cursor()

    check_player_exists(player, cur)

    cur.execute("UPDATE logs SET perma_banned = 0 WHERE player = ?",
                (player, ))
    print(f"[LOGS] Unbanned {player}.")


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
