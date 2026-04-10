N, M = map(int, input().split())
water = [list(map(int, input().split())) for _ in range(N)]

# 초기 구름 위치
cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

#  방향: ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

for _ in range(M):
    di, si = map(int, input().split())

    # 1) 모든 구름이 d방향으로 s칸 이동한다.
    moved_cloud = []
    for r, c in cloud:
        nr = (r + dr[di - 1] * si) % N
        nc = (c + dc[di - 1] * si) % N
        moved_cloud.append((nr, nc))

    # 2) 구름 있는 칸의 바구니 물의 양 += 1
    visited = [[False] * (N) for _ in range(N)]
    for r, c in moved_cloud:
        water[r][c] += 1

        # 3) 모든 구름 없애기 (check 하기)
        visited[r][c] = True

    # 4) 대각선 방향으로 거리 1인 칸에서, 물이 들어있는 바구니 수만큼 (r, c)의 바구니 물 증가
    # 대각선
    diagonal_r = [-1, -1, 1, 1]
    diagonal_c = [-1, 1, 1, -1]
    for r, c in moved_cloud:
        cnt = 0
        for i in range(4):
            nr = r + diagonal_r[i]
            nc = c + diagonal_c[i]
            # 경계 넘어가는 칸은 X
            if 0 <= nr < N and 0 <= nc < N and water[nr][nc] > 0:
                cnt += 1

        water[r][c] += cnt

    # 5) 바구니 물 양이 2 이상인 모든 칸에 구름 생기고, 물 양 -= 2
    # 이때, 구름이 사라졌던 칸은 제외
    cloud = []
    for i in range(N):
        for j in range(N):
            if water[i][j] >= 2 and not visited[i][j]:
                water[i][j] -= 2
                cloud.append((i, j))

# M번 이동 후, 바구니에 있는 물의 합 구하기
ans = 0
for i in range(N):
    ans += sum(water[i])

print(ans)