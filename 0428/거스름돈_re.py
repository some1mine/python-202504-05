amount = int(input("물건값을 입력해주세요, 내는 돈은 10만원이므로 10만원 이하 : "))
arr = [1, 2, 7, 10] #[50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
change = 1000 - amount
# for i in arr:
#     if change // i > 0:
#         print(f"{i:5}짜리 {change // i:2}개"); change %= i
#     if change == 0: break
dp = [99999 for _ in range(amount)]; dp[0] = 0
for i in arr: dp[i] = 1
for i in range(1, amount):
    for j in arr:
        if i > j: dp[i] = min(dp[i], dp[j] + 1)
    print(*dp)
print(*dp)