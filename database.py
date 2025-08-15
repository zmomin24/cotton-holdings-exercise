
import sqlite3 as db

connection = db.connect("cotton.db")

sqlCursor = connection.cursor()

sqlCursor.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")

result = sqlCursor.execute("SELECT name FROM sqlite_master")
print(result.fetchone())
