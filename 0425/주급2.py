#문제1. 주급 계산 : 이름, 근무 시간, 시간당 급여, 추가수당(20시간 초과시 시간당 급여액의 50% 추가지급)

name = input('이름 : '); work_hour = int(input('근무 시간 : ')); hour_pay = int(input('시간당 급여 : '))
if work_hour > 20:
    total_pay = hour_pay * work_hour + hour_pay * (work_hour - 20) // 2
    print(f'{name}님 {work_hour}동안 열심히 일하셔서 {total_pay}원 지급 예정입니다.[20시간 이상 근로를 축하드려요]')
else:
    total_pay = hour_pay * work_hour
    print(f'{name}님 {work_hour}동안 열심히 일하셔서 {total_pay}원 지급 예정입니다.')
    
'''
컴퓨터활용능력시험
이름 필기(400) 워드(200) 스프레드시트(200) 프레젠테이션(200)

총점을 구해 A(800 이상) B(600 이상 800미만) C(400이상 600미만) D(400미만, 재시험 요망)
'''
