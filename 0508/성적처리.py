# 이름 국어 영어 수학 총점 평균 등급     평균으로 수(90) 우(80) 미(70) 양(60) 가(60 미만)

class Student:
    def __init__(self):
        try:
            arr = input('학생의 이름과 국어, 영어, 수학 성적을 입력해주세요(ex tmp 90 80 70) : ').rstrip().split()
            self.name = arr[0]
            self.kor = int(arr[1])
            self.eng = int(arr[2])
            self.math = int(arr[3])
            self.calc()
        except:
            return None
    
    def calc(self):
        self.total = self.kor + self.eng + self.math
        self.avg = self.total / 3
        self.calc_grade()
    
    def calc_grade(self):
        self.grade = '수' if self.avg >= 90 else '우' if self.avg >= 80 else '미' if self.avg >= 70 else '양' if self.avg >= 60 else '가'

    def output(self):
        print(f'{self.name}님 \
            국어 {self.kor} \
              수학 {self.math} \
                영어 {self.eng} \
                    총점 {self.total} \
                        평균 {self.avg:5}으로 \
                            등급은 {self.grade}입니다.')

class Grades:
    def __init__(self):
        self.students = []
        self.grade_statistics = {'수' : 0, '우' : 0, '미' : 0, '양' : 0, '가' : 0}
        self.kor_total = 0
        self.eng_total = 0
        self.math_total = 0

    def add(self, s : Student):
        self.students.append(s)
        self.kor_total += s.kor
        self.eng_total += s.eng
        self.math_total += s.math
        self.grade_statistics[s.grade] += 1

    def output(self):
        for s in self.students: s.output()
    
    def statistics(self):
        print(f'학생들의 \
              국어 평균은 {self.kor_total / len(self.students)} \
              | 영어 평균은 {self.eng_total / len(self.students)} \
                | 수학 평균은 {self.math_total / len(self.students)} \
                    | 등급 분포는 {self.grade_statistics}입니다.')

def main():
    print('=== 학생 성적 시스템 ===')
    g = Grades()
    while True:
        pick = input('메뉴를 골라주세요 0 종료 | 1 성적입력 | 2 학생 성적 목록 조회 | 3 학생 성적 통계 조회 : ').rstrip()
        if pick == '0': return
        if pick == '1':
            s = Student()
            if s is None: print('잘못된 학생 성적 정보 입력입니다.')
            else: g.add(s)
        if pick == '2': g.output()
        if pick == '3': g.statistics()
            
if __name__ == '__main__':
    main()