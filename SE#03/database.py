"""
Copyright (c) 2019 - 2021 Andrey Plugin (9keepa@gmail.com)
Licensed under the MIT License https://github.com/repen/E-parsers/blob/master/License
"""
import sqlite3, os

# PATH = "C:/Users/terminator/Desktop/Scripts/EFS"
PATH = os.getcwd()
NAME = "/myscore.db"

class Database:

    def __init__(self, path):
        # self.path = path # "C:/Users/terminator/Desktop/Scripts/EFS/myscore.db"
        # self.path = PATH + NAME
        self.path = path

    def connect(self):
        return sqlite3.connect(self.path)

    def read(self, sql, **kwargs):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        if kwargs.setdefault("all", False):
            res = cursor.fetchall()
        else:
            res = cursor.fetchone()
        conn.close()
        return res


    def read_iter(self, sql):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor


    def write(self, sql, args = None):
        conn = self.connect()
        cursor = conn.cursor()
        if args:
            cursor.executemany(sql, args)
        else:
            cursor.execute(sql)
        conn.commit()
        conn.close()


if __name__ == '__main__':
    db = Database("/home/repente/prog/python/youtube/parsers/SE00/SE#03/myscore.db")
    db.write("CREATE TABLE match (id_match TEXT, url TEXT, status INTEGER)")
    # result = db.read("SELECT url FROM match", all = True)
    # for url in result:
    #     print(url[0])
