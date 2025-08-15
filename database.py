
import sqlite3 as db

def create_db():
    connection = db.connect("cotton.db")

    sqlCursor = connection.cursor()

    sqlCursor.execute("CREATE TABLE IF NOT EXISTS alerts_by_state"
    "(alert_by_state_id INTEGER PRIMARY KEY," \
    " state text," \
    " count_of_alerts INTEGER," \
    "create_ts DATETIME)")

    result = sqlCursor.execute("SELECT name FROM sqlite_master")
    print(result.fetchone())

create_db()