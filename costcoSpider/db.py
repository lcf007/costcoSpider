from datetime import datetime

import pymysql
import pytz

MYSQL_HOST = '127.0.0.1'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '12345678'
MYSQL_PORT = 3306
MYSQL_DB = 'shoping'
MYSQL_CHARSET = 'utf8mb4'

MYSQL = {
    'host': MYSQL_HOST,
    'port': MYSQL_PORT,
    'user': MYSQL_USER,
    'password': MYSQL_PASSWORD,
    'charset': MYSQL_CHARSET,
    'database': MYSQL_DB
}

def conn_db():
    db_conf = MYSQL
    db_conf['cursorclass'] = pymysql.cursors.DictCursor
    conn = pymysql.connect(**db_conf)
    conn.autocommit(1)
    return conn


def cursor_db(conn):
    return conn.cursor()


class Sql(object):
    conn = conn_db()
    cursor = cursor_db(conn)

    @classmethod
    def fetchDept(cls):
        sql = "SELECT * FROM department"
        cls.cursor.execute(sql)
        item = cls.cursor.fetchall()
        return item

    @classmethod
    def insert_product(cls, prod):
        print("--------------------prod---------------------------------")
        print(prod)
        sql = "INSERT INTO `product`(`url`, `deptid`, `curprice`, `lowprice`, `highprice`)" \
              "VALUES ( '%s', '%d', %d, '%d', '%d')" % \
              (prod['url'], 1, prod['price'], prod['price'], prod['price'])
        try:
            cls.cursor.execute(sql)
            cls.conn.commit()
        except pymysql.MySQLError as e:
            print(e)
            cls.conn.rollback()
        pass



