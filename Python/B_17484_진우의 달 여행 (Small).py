n, m = map(int, input().split())
fuel = [list(map(int, input().split())) for _ in range(n)]

dr = [1, 1, 1]
dc = [-1, 0, 1]
INF = 10**9
# (r,c)에 dir 방향으로 이동g하여 도착했을 때의 최소 연료
dp = [[[INF] * 3 for _ in range(m)] for _ in range(n)]
for c in range(m):
    for dir in range(3):
        dp[0][c][dir] = fuel[0][c]

for r in range(n-1):  # 마지막 행에서는 아래로 못 감
    for c in range(m):
        for dir in range(3):  # 직전 방향
            for ndir in range(3):  # 다음 방향 후보
                if ndir == dir:
                    continue

                nr = r + dr[ndir]
                nc = c + dc[ndir]

                if 0 <= nc < m:
                    dp[nr][nc][ndir] = min(dp[nr][nc][ndir], dp[r][c][dir] + fuel[nr][nc])

ans = min(min(dp[n-1][c]) for c in range(m))
print(ans)