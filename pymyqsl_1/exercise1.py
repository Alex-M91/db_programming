import pymysql
from secrets import *

db = pymysql.connect(host, user, password, "default")
with db.cursor() as c:
    c._defer_warnings = True
    create_stmt = """
    CREATE TABLE IF NOT EXISTS `bikesharing`
    (tstamp TIMESTAMP,
    cnt INTEGER,
    temperature DECIMAL(5, 2),
    temperature_feels DECIMAL(5, 2),
    humidity DECIMAL(4, 1),
    wind_speed DECIMAL(5, 2),
    weather_code INTEGER,
    is_holiday BOOLEAN,
    is_weekend BOOLEAN,
    season INTEGER);
"""
    c.execute(create_stmt)
    db.commit()
db.close()
