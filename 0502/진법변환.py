# 10진수 정수를 2진수, 8진수, 16진수로 각각 변환하기
arr = [15, 17, 68, 127, 356]
flags = ['A', 'B', 'C', 'D', 'E', 'F']
formations = [2, 8, 16]
for j in formations:
    for i in arr:
        result = ''
        while i:
           result += (str(i % j) if i % j < 10 else flags[i % j - 10])
           i //= j
        print(''.join(reversed(result)), end = '\t')
    print()
    