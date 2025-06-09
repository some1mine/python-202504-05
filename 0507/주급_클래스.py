'''
주급 : 이름, 시간당 급여, 근무 시간
'''

class Worker:
    def __init__(self, name = '', wage = 10, work_hour = 10):
        self.name = name
        self.wage = int(wage)
        self.work_hour = int(work_hour)
        self.process()
    
    def process(self):
        self.total = self.wage * self.work_hour

    def output(self):
        print(f'{self.name}님은 시간당 {self.wage}원을 받으며 {self.work_hour}시간 일한 결과 총 {self.total}원 지급 예정입니다.')

w1 = Worker(*input('주급을 입력할 사람의 정보를 입력해주세요(이름 시간당급여 근무시간 형식, ex 김길준 10030 30) :').split())
w2 = Worker(*input('주급을 입력할 사람의 정보를 입력해주세요(이름 시간당급여 근무시간 형식, ex 김길준 10030 30) :').split())

w1.output()
w2.output()

'''
wList = [
    Worker('홍길동', 20, 40000),
    Worker('박길동', 10, 60000),
    Worker('김길동', 30, 50000),
    Worker('이길동', 40, 30000),
    Worker('장길동', 20, 20000)
]

for w in wList: w.output()
'''

class WorkerManger:
    def __init__(self):
        self.worker_list = [
            Worker('홍길동', 20, 40000),
            Worker('박길동', 10, 60000),
            Worker('김길동', 30, 50000),
            Worker('이길동', 40, 30000),
            Worker('장길동', 20, 20000)
        ]
    
    def output(self):
        for w in self.worker_list: w.output()

mgr = WorkerManger()
mgr.output()