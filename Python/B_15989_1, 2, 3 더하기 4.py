t = int(input())
Ns = [int(input()) for _ in range(t)]
maxN = max(Ns)

dp = [0] * (maxN + 1)
dp[0] = 1
num = [1, 2, 3]
for n in num:
    for i in range(n, maxN+1):
        dp[i] += dp[i-n]

for i in Ns:
    print(dp[i])