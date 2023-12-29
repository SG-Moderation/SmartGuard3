import sqlite3


def create_database():
  with sqlite3.connect("mod_db.sqlite") as conn:
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS logs (
      id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
      player TEXT UNIQUE NOT NULL,
      action_taken INTEGER NOT NULL,
      temp_bans INTEGER NOT NULL,
      perma_banned INTEGER
    )""")


def debug():
  with sqlite3.connect("mod_db.sqlite") as conn:
    cur = conn.cursor

    try:
      cur.execute("""
    INSERT INTO logs (
      player, action_taken, temp_bans, perma_banned
      ) VALUES ('s20', 2, 0, 0)
    """)
    except IntegrityError:
      print("It exists why are you irritating me")

    cur.execute("SELECT * FROM logs")
    rows = cur.fetchall()
    for row in rows:
      print(row)
