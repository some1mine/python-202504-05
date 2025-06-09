class Weekpay:
    def __init__(self, name = '', wage = 10, work_hour = 10):
        self.name = name
        self.wage = int(wage)
        self.work_hour = int(work_hour)
        self.process()
    
    def process(self):
        self.total = self.wage * self.work_hour

    def output(self):
        print(f'{self.name}님은 시간당 {self.wage}원을 받으며 {self.work_hour}시간 일한 결과 총 {self.total}원 지급 예정입니다.')

if __name__ == '__main__':
    w1 = Weekpay('A')
    w1.output()