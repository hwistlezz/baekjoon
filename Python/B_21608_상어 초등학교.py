n = int(input())
info = [list(map(int, input().split())) for _ in range(n * n)]

graph = [[-1] * n for _ in range(n)]
# 인접 칸 (동서남북)
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

for i in range(n*n):
    student = info[i][0]
    likes = info[i][1:]

    candidate1= []
    # 규칙 1: 좋아하는 학생이 인접한 칸에 가장 많은 칸 선택
    max_like_cnt = 0
    for r in range(n):
        for c in range(n):
            if graph[r][c] == -1:  #비어있는 칸일 때
                like_cnt = 0
                for x in range(4):
                    nr = r + dr[x]
                    nc = c + dc[x]
                    if 0 <= nr < n and 0 <= nc < n:
                        if graph[nr][nc] in likes:
                            like_cnt += 1

                if max_like_cnt < like_cnt:
                    max_like_cnt = like_cnt
                    candidate1 = [(r, c)]
                elif max_like_cnt == like_cnt:
                    candidate1.append((r, c))

    if len(candidate1) == 1:
        r, c = candidate1.pop()
        graph[r][c] = student
        continue
    # 규칙 2: 후보 여러 개 -> 인접한 칸 중에서 비어있는 칸이 가장 많은 칸 선택
    candidate2 = []
    max_empty_cnt = 0
    for r, c in candidate1:
        empty_cnt = 0

        for x in range(4):
            nr = r + dr[x]
            nc = c + dc[x]
            if 0 <= nr < n and 0 <= nc < n:
                if graph[nr][nc] == -1:
                    empty_cnt += 1

        if max_empty_cnt < empty_cnt:
            max_empty_cnt = empty_cnt
            candidate2 = [(r, c)]
        elif max_empty_cnt == empty_cnt:
            candidate2.append((r, c))

    if len(candidate2) == 1:
        r, c = candidate2.pop()
        graph[r][c] = student
        continue
    # 규칙 3: 후보 여러 개 -> 행의 번호가 가장 작은 칸 -> 열의 번호가 가장 작은 칸
    candidate2.sort()
    r, c = candidate2[0]
    graph[r][c] = student

# 만족도 구하기
ans = 0
for r in range(n):
    for c in range(n):
        like_cnt = 0

        for i in range(n * n):
            if info[i][0] == graph[r][c]:
                likes = info[i][1:]
                break

        for x in range(4):
            nr = r + dr[x]
            nc = c + dc[x]
            if 0 <= nr < n and 0 <= nc < n:
                if graph[nr][nc] in likes:
                    like_cnt += 1

        if like_cnt == 0:
            continue
        elif like_cnt == 1:
            ans += 1
        elif like_cnt == 2:
            ans += 10
        elif like_cnt == 3:
            ans += 100
        elif like_cnt == 4:
            ans += 1000

print(ans)