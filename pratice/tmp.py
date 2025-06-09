n = int(input()); num = list(map(int, input()))
for i in range(1, n):
    if num[i] != num[i - 1]: num[i] = 1
    else: num[i] = 0
print(''.join(str(i) for i in num))