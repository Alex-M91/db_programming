import pymysql
from secrets import *

db = pymysql.connect(host, user, password, "default")
with db.cursor() as c:
    c._defer_warnings = True
    insert_stm = """
    INSERT INTO `bikesharing`
    (timestamp,cnt,temperature,temperature_feels,humidity,wind_speed,weather_code,is_holiday,is_weekend,season)
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    filename = 'london-bikes.csv'
    with open(filename, 'r') as ff:
        lines = ff.readlines()
        count = 0
        for line in lines :
            print("Line {} : {} ".format(count, line.split()))
            count += 1
            values = line.split()
        if count > 0 and count % 100 == 0:
            db.commit()
    db.commit()
db.close()
