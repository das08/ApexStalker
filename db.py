import sqlite3

DBNAME = "apex.db"


def createUserTable():
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()

    cur.execute("create table user_data(uid string primary key, platform string, level integer, trio_rank integer, arena_rank integer, last_update number);")

    conn.commit()
    conn.close()


def selectUID(tableName: str, uid: str):
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()

    if uid != "":
        cur.execute(f"SELECT * FROM {tableName} WHERE uid = '{uid}'")
    else:
        cur.execute(f"SELECT * FROM {tableName}")
    res = cur.fetchall()

    conn.commit()
    conn.close()
    return res


def insert(tableName: str, kv: dict, upSert=False):
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()

    keys: list = []
    vals: list = []
    keysStmt: str = ""
    valsStmt: str = ""

    for k in kv.keys():
        keys.append(k)
        vals.append(kv[k])

    keysStmt = ",".join(keys)
    for idx in range(len(vals)):
        if type(vals[idx]) == str:
            valsStmt += f"\'{vals[idx]}\'"
        else:
            valsStmt += f"{vals[idx]}"
        if idx != len(vals) - 1:
            valsStmt += ","

    if upSert:
        cur.execute(f"REPLACE INTO {tableName} values({valsStmt})")
    else:
        cur.execute(f"INSERT INTO {tableName} values({valsStmt})")

    conn.commit()
    conn.close()


def delete(tableName: str, uid: str):
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()

    cur.execute(f"DELETE FROM {tableName} where uid = '{uid}'")

    conn.commit()
    conn.close()


def dropTable(tableName: str):
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()

    cur.execute(f"DROP TABLE {tableName}")

    conn.commit()
    conn.close()
