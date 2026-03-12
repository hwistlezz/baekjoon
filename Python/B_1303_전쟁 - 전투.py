from collections import deque

n, m = map(int, input().split())
graph = [input() for _ in range(m)]

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
visited = [[False] * n for _ in range(m)]


def bfs(sr, sc):
    color = graph[sr][sc]
    q = deque([(sr, sc)])
    visited[sr][sc] = True
    cnt = 1

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < m and 0 <= nc < n:
                # 시작 칸 색을 기준으로 같은 색만 확장
                if not visited[nr][nc] and graph[nr][nc] == color:
                    q.append((nr, nc))
                    visited[nr][nc] = True
                    cnt += 1

    return cnt


w_power = 0
b_power = 0

for r in range(m):
    for c in range(n):
        if not visited[r][c]:
            cnt = bfs(r, c)
            if graph[r][c] == 'W':
                w_power += (cnt * cnt)
            elif graph[r][c] == 'B':
                b_power += (cnt * cnt)

print(w_power, b_power)