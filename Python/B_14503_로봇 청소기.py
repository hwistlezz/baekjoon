from collections import deque
n, m = map(int, input().split())
sr, sc, d = map(int, input().split())
# 북동남서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

cnt = 0


def bfs(sr, sc, d):
    global cnt

    q = deque([(sr, sc, d)])
    if graph[sr][sc] == 0 and not visited[sr][sc]:
        visited[sr][sc] = True
        cnt += 1

    while q:
        r, c, d = q.popleft()

        if graph[r][c] == 0 and not visited[r][c]:
            visited[r][c] = True
            cnt += 1

        can_clean = False
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if graph[nr][nc] == 0 and not visited[nr][nc]:
                can_clean = True
                break

        if not can_clean:
            nr = r - dr[d]
            nc = c - dc[d]
            if graph[nr][nc] != 1:
                q.append((nr, nc, d))
                continue
            else:  # 후진하는 곳이 벽이면 작동 멈춤
                print(cnt)
                exit()
        else:
            while True:
                d = (d - 1) % 4  # 반시계 방향으로 90도 회전
                nr = r + dr[d]
                nc = c + dc[d]
                # 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진
                if graph[nr][nc] == 0 and not visited[nr][nc]:
                    q.append((nr, nc, d))
                    break


bfs(sr, sc, d)
print(cnt)