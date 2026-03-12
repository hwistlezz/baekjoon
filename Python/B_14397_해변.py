from collections import deque

n, m = map(int, input().split())
graph = [input() for _ in range(n)]

# 홀/짝 행마다 방향 다름
even_dirs = [(-1, -1), (0, -1), (1, -1), (1, 0), (0, 1), (-1, 0)]
odd_dirs = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1)]

beach_length = 0

for r in range(n):
    for c in range(m):
        # '.'은 물, '#'은 땅
        if graph[r][c] == '.':  # 물(.)은 Skip
            continue

        if r % 2 == 0:  # 짝수행이면
            dirs = even_dirs
        else:           # 홀수행이면
            dirs = odd_dirs

        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < n and 0 <= nc < m:
                if graph[nr][nc] == '.':  # 땅 -> 물 만나면 증가
                    beach_length += 1

print(beach_length)