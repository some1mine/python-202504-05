from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine(
    'mysql+pymysql://root:1234@localhost/mydb',
    pool_size = 10,
    max_overflow = 5,
    pool_recycle = 3600
)


class ScoreData:
    def __init__(self, sname = '', kor = 0, eng = 0, math = 0, total = 0, average = 0):
        self.sname = sname
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = total
        self.average = average

    def output(self):
        print(self.sname, self.kor, self.eng, self.math, self.total, self.average)

class ScoreManager:
    def __init__(self):
        self.conn = engine.connect()

    def append(self):
        sname = input('이름 : ')
        kor = int(input('국어 : '))
        eng = int(input('영어 : '))
        math = int(input('수학 : '))
        score = ScoreData(sname, kor, eng, math, kor + eng + math, (kor + eng + math) / 3)
        sql = text('''
            insert into tb_score(sname, kor, eng, math, regdate) values(:sanme, :kor, :eng, :math, :kor, :total, :average, now())
        ''')
        self.conn.execute(sql, (score.sname, score.kor, score.eng, score.math))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def output(self):
        sql = 'select * from tb_score'
        rows = self.db.execute(sql)
        print(rows)

if __name__ == '__main__':
    sm = ScoreManager()
    sm.output()