from secrets import *
import pymysql

db = pymysql.connect(host, user , password, "")     # ultimul parametru reprezinta baza de date
with db.cursor() as c:
    c._defer_warnings = True    # daca avem warnings , nu le mai ia in considerare
    c.execute("CREATE SCHEMA IF NOT EXISTS `default` DEFAULT CHARACTER SET utf8;")
db.close()

db = pymysql.connect(host, user, password, "default")
db.close()
