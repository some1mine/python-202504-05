from DBModule import Database

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
        self.db = Database()

    def append(self):
        sname = input('이름 : ')
        kor = int(input('국어 : '))
        eng = int(input('영어 : '))
        math = int(input('수학 : '))
        score = ScoreData(sname, kor, eng, math, kor + eng + math, (kor + eng + math) / 3)
        sql = '''
            insert into tb_score(sname, kor, eng, math, regdate) values(%s, %s, %s, %s, now())
        '''
        self.db.executeOne(sql, (score.sname, score.kor, score.eng, score.math))
        self.db.db.commit()

    def __del__(self):
        self.db.close()

    def output(self):
        sql = 'select * from tb_score'
        rows = self.db.executeAll(sql)
        print(rows)

if __name__ == '__main__':
    sm = ScoreManager()
    sm.output()