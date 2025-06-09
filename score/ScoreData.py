class ScoreData:
    def __init__(self, name = '홍길동', kor = 100, eng = 100, math = 100):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.process()

    def process(self):
        self.total = self.kor + self.eng + self.math
        self.avg = self.total / 3
        self.grade = '수' if self.avg >= 90 else '우' if self.avg >= 80 else '미' if self.avg >= 70 else '양' if self.avg >= 60 else '가'

    def print(self):
        print(self.name, self.kor, self.eng, self.math, self.total, f'{self.avg:.2f}', self.grade, sep = '\t')

if __name__ == '__main__':
    s = ScoreData()
    s.print()