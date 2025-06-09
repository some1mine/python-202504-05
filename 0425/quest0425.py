#문제1. 정수 5개를 입력 받아 합계를 구하라
print(sum(int(input(f'합계를 구할 5개 정수중 {i}번째 정수 : ')) for i in range(1, 6)))

#문제2. 숫자 10개를 입력받아 짝수와 홀수의 합과 평균을 구하기
odds = []; evens = []
for i in range(10):
    a = int(input(f'짝/홀을 구분해 합계와 평균을 구할 10개 정수중 {i + 1}번째 정수 : '))
    if a % 2: odds.append(a)
    else: evens.append(a)
print(f'odds, sum : {sum(odds)} | avg : {sum(odds) / len(odds)}')
print(f'evens, sum : {sum(evens)} | avg : {sum(evens) / len(evens)}')