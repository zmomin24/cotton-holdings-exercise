
import sqlite3 as db

def create_db():
    connection = db.connect("cotton.db")

    sqlCursor = connection.cursor()

    sqlCursor.execute("CREATE TABLE IF NOT EXISTS alerts_by_state"
    "(alert_by_state_id INTEGER PRIMARY KEY," \
    " state TEXT," \
    " count_of_alerts INTEGER," \
    "create_ts DATETIME)")

    sqlCursor.execute("CREATE TABLE IF NOT EXISTS all_alerts_data"
    "(all_alerts_data_id INTEGER PRIMARY KEY AUTOINCREMENT," \
    "id TEXT," \
    "event TEXT," \
    "severity TEXT," \
    "urgency TEXT," \
    "state TEXT," \
    "sent_ts DATETIME," \
    "expire_ts DATETIME," \
    "record_create_ts DATETIME)")
    

    result = sqlCursor.execute("SELECT name FROM sqlite_master")
    print(result.fetchall())

create_db()

