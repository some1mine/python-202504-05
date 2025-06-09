class Worker:
    def __init__(self, name, wage, workHour):
        self.name = name
        self.wage = wage
        self.workHour = workHour
        self.process()
    
    def process(self):
        self.plusWage = self.workHour // 40 * 8 * self.wage
        self.total = self.wage * self.workHour + self.plusWage

    def output(self):
        print(f'시간당 {self.wage}원을 받으며 {self.workHour}시간 일한 결과 주휴수당 {self.plusWage}원을 포함해 총 {self.total}원 지급 예정인 {self.name}님 고생 많으셨습니다.')