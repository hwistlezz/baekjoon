import sys
input = sys.stdin.readline

N = int(input())
T = [0] * N
P = [0] * N
for i in range(N):
    T[i], P[i] = map(int, input().split())

dp = [0] * (N+1)
for i in range(N-1, -1, -1):  # 마지막 날부터 시작
    if i + T[i] <= N:  # 상담이 가능한 경우
        # dp[i] = max(i번째날 상담 O, i번째날 상담 X)
        dp[i] = max(dp[i + T[i]] + P[i], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])