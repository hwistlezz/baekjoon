n = int(input())  # 포도주 잔 개수
wine = [0] * (n+1)
for i in range(1, n+1):
    wine[i] = int(input())

dp = [0] * (n+1)

if n >= 1:
    dp[1] = wine[1]
if n >= 2:
    dp[2] = wine[1] + wine[2]

for i in range(3, n+1):
    dp[i] = max(
        dp[i-1],                       # i 안 마심
        dp[i-2] + wine[i],             # i만 마심(i-1 제외)
        dp[i-3] + wine[i-1] + wine[i]  # i-1, i 둘 다 마심
    )

print(dp[n])