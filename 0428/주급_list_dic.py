person_list = [{'name':'홍길동', 'work_time' : 40, 'per_pay' : 10000},
               {'name':'임꺽정', 'work_time' : 30, 'per_pay' : 20000},
               {'name':'장길산', 'work_time' : 20, 'per_pay' : 30000},
               ]

#추가하기
for _ in range(5):
    worker = {} #한 사람분 저장하기
    worker['name'] = input('이름 : ')
    worker['work_time'] = int(input('일한 시간 : '))
    worker['per_pay'] = int(input('시간당 급여액 : '))
    person_list.append(worker)
    
for worker in person_list:
    worker['pay'] = worker['work_time'] * worker['per_pay']
for worker in person_list:
    print(f"{worker['name']}님은 {worker['work_time']}시간 일하며 시간당 {worker['per_pay']}원 받아 총 {worker['pay']}원 벌었습니다.")