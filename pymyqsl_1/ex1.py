from secrets import *
import pymysql

db = pymysql.connect(host, user, password, "")

with db.cursor() as c:
    c._defer_warnings = True
    c.execute("SELECT VERSION()")
    version = c.fetchone()
    print(f"Database version: {version[0]}")
db.close()
