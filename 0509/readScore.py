import sys; import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../score')))
import ScoreData as ScoreData

class ScoreData:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = int(kor)
        self.eng = int(eng)
        self.math = int(math)
        self.process()

    def process(self):
        self.total = self.kor + self.eng + self.math
        self.avg = self.total / 3
        self.grade = '수' if self.avg >= 90 else '우' if self.avg >= 80 else '미' if self.avg >= 70 else '양' if self.avg >= 60 else '가'

    def print(self):
        print(self.name, self.kor, self.eng, self.math, self.total, f'{self.avg:.2f}', self.grade, sep = '\t')
        
students = []
with open('file/score.txt', 'r', encoding = 'utf-8') as file:
    for s in [*map(lambda x: x.rstrip().split(','), file.readlines())] : students.append(ScoreData(*s))

for s in students: s.print()