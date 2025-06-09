#1~10까지의 합 구하기
#변수 1~10까지 변하는 변수
#더해지는 값 - 누적값을 저장할 변수가 필요하다.
total = 0; limit = int(input('1부터 합계를 구할 양수를 입력해주세요 : '))
for i in range(1, limit + 1):
    total += i
    print(f'i={i:3} total={total:3}')
    