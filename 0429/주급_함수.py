#함수 동작 확인을 위해서는 출력 확인부터 하는 것이 좋다는 말씀

worker_list = [
    {'name' : '홍길동', 'work_time' : 30, 'hour_wage' : 20000},
    {'name' : '김길동', 'work_time' : 20, 'hour_wage' : 30000},
    {'name' : '고길동', 'work_time' : 50, 'hour_wage' : 20000}
] #전역 변수로 존재해야 함

def append(): #데이터 추가 함수
    worker = {} #dict 타입 객체 생성
    worker['name'] = input('이름 : ')
    worker['work_time'] = int(input('일한 시간 : '))
    worker['hour_wage'] = int(input('시간당 급여액 : '))
    worker_list.append(worker)

def output():
    for w in worker_list: print(f"{w['name']:10}님은{w['work_time']:3}시간동안\t{w['hour_wage']:6}원씩 받으며 총{w['total_pay']:18}원을 받았습니다")

append()
def process(worker):
    worker['total_pay'] = worker['work_time'] * worker['hour_wage']
for w in worker_list:
    process(w)
print(*worker_list)
output()

def main():
    #return 반환값을 외부로 전달하며 함수 종료
    #return문이 없더라도 내부 로직을 모두 지나면 함수 종료
    while True:
        print('1.추가')
        print('2.출력')
        print('0.종료')
        sel = input('선택 : ')
        if sel == '1': append()
        elif sel == '2': output()
        elif sel == '0':
            print('프로그램을 종료합니다.')
            return 
main()