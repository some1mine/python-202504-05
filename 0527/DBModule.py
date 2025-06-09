import pymysql
import pymysql.cursors

class Database:
    def __init__(self):
        self.db = pymysql.connect(
            host = 'localhost',
            port = 3306,
            user = 'user03',
            passwd = '1234',
            db = 'project1'
        )
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def executeOne(self, query, args = ()):
        print(args)
        self.cursor.execute(query, args)
        return self.cursor.fetchone()
    
    def executeAll(self, query, args = ()):
        print(args)
        self.cursor.execute(query, args)
        return self.cursor.fetchall()
    
    def close(self):
        if self.db.open: self.db.close()