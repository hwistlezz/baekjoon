n = int(input())

graph = [[0] * (101) for _ in range(101)]
# → / ↑ / ← / ↓
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

for _ in range(n):
    sc, sr, direction, gen = map(int, input().split())

    # 규칙 찾기: 끝점(좌표) 기준으로 변화 관찰
    # 1) 0: x좌표가 증가하는 방향 (→)
    # 3, 3 -> 3,4 -> 2, 4
    # c (+) -> r (-)  # 끝점 기준

    # 2) 1: y좌표가 감소하는 방향 (↑)
    # 2, 3 -> 1, 3 -> 1, 2
    # r (-) -> c (-)  # 끝점 기준

    # 3) 2: x좌표가 감소하는 방향 (←)
    # 2, 4 -> 2, 3 -> 3, 3
    # c (-) -> r (+)  # 끝점 기준

    # 4) 3: y좌표가 증가하는 방향 (↓)
    # 3,3 -> 4, 3 -> 4, 4
    # r (+) -> c (+)  # 끝점 기준

    # 0세대 생성
    arr = [(sr, sc)]  # 시작 위치
    nr = sr + dr[direction]
    nc = sc + dc[direction]
    arr.append((nr, nc))  # 0세대 끝점

    for _ in range(gen):  # 세대 반복
        end_r, end_c = arr[-1]  # 끝점 기준
        for i in range(len(arr) - 2, -1, -1):
            cur_r, cur_c = arr[i]
            arr.append((end_r - (end_c - cur_c), end_c + (end_r - cur_r)))

    for r, c in arr:
        graph[r][c] = 1

# 2*2 네 칸이 모두 1 사각형 개수 세기
ans = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == graph[i+1][j] == graph[i][j+1] == graph[i+1][j+1] == 1:
            ans += 1

print(ans)