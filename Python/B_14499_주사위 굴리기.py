n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
op = list(map(int, input().split()))

# 동서북남
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

# 주사위: [top, bottom, north, south, east, west]
dice = [0, 0, 0, 0, 0, 0]

for dir in op:
    # 다음 움직일 곳
    nx = x + dr[dir - 1]
    ny = y + dc[dir - 1]

    if 0 <= nx < n and 0 <= ny < m:  # 범위 체크
        x += dr[dir - 1]
        y += dc[dir - 1]

        if dir == 1:    # 동쪽
            temp = dice.copy()
            dice[4] = temp[0]  # east <- top
            dice[1] = temp[4]  # bottom <- east
            dice[5] = temp[1]  # west <- bottom
            dice[0] = temp[5]  # top <- west
        elif dir == 2:  # 서쪽
            temp = dice.copy()
            dice[5] = temp[0]  # west <- top
            dice[1] = temp[5]  # bottom <- west
            dice[4] = temp[1]  # east <- bottom
            dice[0] = temp[4]  # top <- east
        elif dir == 3:  # 북쪽
            temp = dice.copy()
            dice[2] = temp[0]  # north <- top
            dice[1] = temp[2]  # bottom <- north
            dice[3] = temp[1]  # south <- bottom
            dice[0] = temp[3]  # top <- south
        elif dir == 4:  # 남쪽
            temp = dice.copy()
            dice[3] = temp[0]  # south <- top
            dice[1] = temp[3]  # bottom <- south
            dice[2] = temp[1]  # north <- bottom
            dice[0] = temp[2]  # top <- north

        if graph[x][y] == 0:
            graph[x][y] = dice[1]  # graph <- bottom
        else:  # graph[x][y] != 0
            dice[1] = graph[x][y]  # bottom <- graph
            graph[x][y] = 0

        print(dice[0])
    else:
        continue