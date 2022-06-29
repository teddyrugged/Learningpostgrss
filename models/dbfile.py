import psycopg2
import sqlite3
import os

class DBFile:

    @staticmethod
    def connect():
        # conn = None
        try:
            conn = psycopg2.connect(
                host='localhost', user='postgres', password='Holycraft@30',
                dbname='my_db_decagon', port=os.getenv("PORT"))

            return conn
        except Exception as err:
            print(f'connection failed.Error {err}')
            # middle man


class SQliteDb:

    @staticmethod
    def connect():
        conn = None
        try:
            conn = sqlite3.connect('graded.sqlite')
            return conn
        except Exception as err:
            print(f'connection failed.Error {err}')
    # cur = conn.cursor()
    #
    # sql = """SELECT * FROM users_table;"""
    # cur.execute(sql)
    #
    # for details in cur.fetchall():
    #     print(details)
    #
    # # insert
    # # sql = """INSERT INTO users_table (id,username,lastname, firstname, created_at, updateded_at)
    # # VALUES  (3,'delilah', 'kitigo','sampson','1-2-2005', '1-4-2005')"""
    # # cur.execute(sql)
    #
    # # update
    # # sql = """UPDATE users_table SET username = 'ufanabasi' WHERE id = 2 """
    #
    # # # delete
    # sql = """DELETE FROM users_table where id = 1"""
    # cur.execute(sql)
    #
    # conn.commit()
    #
    # cur.close()
    # conn.close()
