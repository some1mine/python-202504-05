even_sum = 0; odd_sum = 0

number_list = [] #리스트 생성

#1. 입력하기
for _ in range(4): number_list.append(int(input('정수를 입력해주세요 :')))

#2. 계산하기
for n in number_list:
    if n % 2: odd_sum += n
    else: even_sum += n

#3. 출력하기
print(even_sum); print(odd_sum)