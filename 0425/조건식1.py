#정수를 하나 입력받아서 양수일 경우 원래 값에 5를 곱해 출력해라
n = int(input('정수 : '))
if n > 0: 
    n *= 5
print(n)

#양수이면 양수, 음수나 0일 경우 양수 아님
if n > 0: print('양수')
else: print('양수 아님')

#양수이면 양수, 0이면 0, 음수이면 음수
if n > 0: print('양수')
elif n == 0:print(0)
else: print('음수')

#문제1. 주급 계산 : 이름, 근무 시간, 시간당 급여, 추가수당(20시간 초과시 시간당 급여액의 50% 추가지급)