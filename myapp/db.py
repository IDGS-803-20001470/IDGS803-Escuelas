from decouple import config

import pymysql

def get_connection():
    connection = pymysql.connect(host=config('MYSQL_HOST'),
                                 user=config('MYSQL_USER'),
                                 password=config('MYSQL_PASSWORD'),
                                 database=config('MYSQL_DB'),
                                 charset='utf8mb4')
    return connection