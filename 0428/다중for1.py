#for문 안의 for문 구조
#외부 * 내부 번 반복
#가급적 2 depth까지

# for i in range(1, 6):
#     for j in range(1, 6):
#         print(f'i = {i}, j = {j}')

#문제1. 이중 for문 사용해서 1~100까지 한 줄에 10개씩 출력하기
# for i in range(10):
#     for j in range(10):
#         print(i * 10 + j + 1, end = '\t')
#     print()

#문제2. 이중 for문
'''
#   1 = 1
#   1 + 2   = 3
#   1 + 2 + 3 = 6
#   1 + 2 + 3 + 4 = 10
#   1 + 2 + 3 + 4 + 5 = 15 .....
'''
# for i in range(1, 11):
#     for j in range(1, i + 1): 
#         print(j, '+' if j < i else '=', end = ' ')
#     print(sum(range(i + 1)))

# for i in range(10): print('*' * (i + 1))

'''
   *
  ***
 *****
*******
 *****
  ***
   *
greedy, dfs, bfs, floyd-warshall
'''
# for i in range(4):
#     print(' ' * (4 - i) + '*' * (i * 2 + 1))
# for i in range(3):
#     print(' ' * (i + 2) + '*' * (5 - 2 * i))
# n = int(input('다이아몬드 모양 출력의 라인 수를 입력해주세요(홀수) : '))
# for i in range(n):
#     if i < n // 2 + 1: print(' ' * (n // 2 - i) + '*' * (i * 2 + 1))
#     else: print(' ' * (i - n // 2) + '*' * (n * 2 - i * 2 - 1))

LINES = 3
# for i in range(1, LINES + 1):
#     print(' ' * (LINES - i), end = '')
#     print('*' * (2 - i - 1))
for i in range(1, LINES + 1):
    for j in range(0, (LINES - i)):
        print(' ', end = '')
    for j in range(0, 2 * i - 1):
        print('*', end = '')
    print()

LINES -= 1
for i in range(1, LINES + 1):
    for j in range(0, i):
        print(' ', end = '')
    for j in range(0, (LINES - i) * 2 + 1):
        print('*', end = '')
    print()