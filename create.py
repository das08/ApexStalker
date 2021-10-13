import sqlite3

DBNAME = "apex.db"


def createTable(tableName: str):
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()

    cur.execute(f"CREATE TABLE {tableName}(uid STRING PRIMARY KEY, rank INTEGER, last_update INTEGER)")

    conn.commit()
    conn.close()


createTable("user_data")
