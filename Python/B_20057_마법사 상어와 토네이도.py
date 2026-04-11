N = int(input())
sands = [list(map(int, input().split())) for _ in range(N)]

# 방향: 좌 하 우 상 순서로
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]
direction = 0  # 방향: 좌(0) 하(1) 우(2) 상(3)

sr, sc = N//2, N//2
nr = sr
nc = sc

# 위 -> 10%: (nr-1, nc-1), 7%: (nr-1, nc), 1%: (nr-1, nc+1), 2%: (nr-2, nc)
# 아래 -> 10%: (nr+1, nc-1), 7%: (nc+1, nc), 1%: (nr+1, nc+1), 2%: (nr+2, nc)
# 같은 행 -> 5%: (nr, nc-2), a(남은 양): (nr, nc-1)
neighbor = [(-1, -1), (-1, 0), (-1, 1), (-2, 0),
            (1, -1), (1, 0), (1, 1), (2, 0),
            (0, -2), (0, -1)]
ratios = [10, 7, 1, 2,
          10, 7, 1, 2,
          5, 0]


def rotation():  # 반시계 방향으로 90도 회전
    # 회전 중심 기준으로
    # r + -> c - /// r - -> c +
    # c + -> r + /// c - -> r -
    for i in range(10):
        change_r = 0 + (0 - neighbor[i][1])
        change_c = 0 - (0 - neighbor[i][0])
        neighbor[i] = (change_r, change_c)


ans = 0  # 격자 밖으로 나간 모래 양
num = 1  # 현재 방향으로 이동하는 칸의 개수
cnt = 0  # 현재 num으로 몇 번 이동했는지 체크
while True:
    if nr == 0 and nc == 0:
        break

    # 현재 방향으로 num칸 만큼 이동 (방향 바꾸면서 2번 반복)
    for i in range(num):
        nr = nr + dr[direction]
        nc = nc + dc[direction]

        # 다음 이동하는 칸에 있는 모래를 주변에 나눠줌
        divide_sand = sands[nr][nc]
        sands[nr][nc] = 0

        if nr == 0 and nc == 0:
            if divide_sand == 0:
                break

        if divide_sand == 0:
            continue

        use_sand = 0
        for (r, c), ratio in zip(neighbor, ratios):
            tr, tc = nr+r, nc+c
            if 0 <= tr < N and 0 <= tc < N:  # 격자 안에 있을 경우
                if ratio == 0:  # 알파는 남은 모래를 다 줌
                    sands[tr][tc] += (divide_sand - use_sand)
                else:
                    divide = divide_sand * ratio // 100
                    sands[tr][tc] += divide
                    use_sand += divide
            else:  # 격자 밖이면 ans에 모래 추가
                if ratio == 0:  # 알파는 남은 모래를 다 줌
                    ans += (divide_sand - use_sand)
                else:
                    divide = divide_sand * ratio // 100
                    ans += divide
                    use_sand += divide

        if nr == 0 and nc == 0:
            break
    # for문 끝 (num칸 만큼 이동)

    direction = (direction+1) % 4
    rotation()  # 반시계 방향으로 90도 회전

    if num < N:  # num == N 이면, (1, 1) 도착할 때까지 num칸씩 이동하면서 방향 바꾸기
        cnt += 1

    if cnt == 2:  # num칸 이동을 2번 반복하면
        num += 1
        cnt = 0

print(ans)