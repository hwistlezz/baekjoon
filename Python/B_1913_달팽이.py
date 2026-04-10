n = int(input())
target = int(input())

# 위 -> 오른쪽 -> 아래 -> 왼쪽 -> 위
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

graph = [[0] * n for _ in range(n)]
r = n // 2
c = n // 2
graph[r][c] = 1

x, y = 0, 0
if target == 1:
    x, y = r + 1, c + 1

num = 1
cnt = 1
dir = 0


# up 1 right 1 / down 2 left2 / up 3 right 3 / down 4 left 4 / up 5 right 5
while num < n * n:
    for _ in range(2):
        for _ in range(cnt):
            r += dr[dir]
            c += dc[dir]

            num += 1
            graph[r][c] = num

            if num == target:
                x, y = r + 1, c + 1

            if num == n * n:
                break

        if num == n * n:
            break

        dir = (dir + 1) % 4

    cnt += 1

for k in range(n):
    print(*graph[k])

print(x, y)