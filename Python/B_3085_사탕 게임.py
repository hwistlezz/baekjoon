n = int(input())
candies = [list(input()) for _ in range(n)]

# 동서남북
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

max_candies = -1
for r in range(n):
    for c in range(n):
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < n and 0 <= nc < n:
                # 스왑
                candies[r][c], candies[nr][nc] = candies[nr][nc], candies[r][c]

                # 1-1) 행 검사 (스왑하는 두 위치 검사)
                cnt = 1
                for j in range(1, n):
                    if candies[r][j] == candies[r][j-1]:
                        cnt += 1
                    else:
                        if cnt > max_candies:
                            max_candies = cnt

                        cnt = 1
                if cnt > max_candies:
                    max_candies = cnt
                # 1-2) 행 검사 (스왑하는 두 위치 검사)
                cnt = 1
                for j in range(1, n):
                    if candies[nr][j] == candies[nr][j-1]:
                        cnt += 1
                    else:
                        if cnt > max_candies:
                            max_candies = cnt

                        cnt = 1
                if cnt > max_candies:
                    max_candies = cnt

                # 2-1) 열 검사 (스왑하는 두 위치 검사)
                cnt = 1
                for i in range(1, n):
                    if candies[i][c] == candies[i-1][c]:
                        cnt += 1
                    else:
                        if cnt > max_candies:
                            max_candies = cnt

                        cnt = 1

                if cnt > max_candies:
                    max_candies = cnt

                # 2-2) 열 검사 (스왑하는 두 위치 검사)
                cnt = 1
                for i in range(1, n):
                    if candies[i][nc] == candies[i-1][nc]:
                        cnt += 1
                    else:
                        if cnt > max_candies:
                            max_candies = cnt

                        cnt = 1
                if cnt > max_candies:
                    max_candies = cnt

                # 스왑 복구
                candies[r][c], candies[nr][nc] = candies[nr][nc], candies[r][c]


print(max_candies)