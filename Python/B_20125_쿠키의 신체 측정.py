import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input().strip()) for _ in range(n)]

find_head = False
heart_x, heart_y = 0, 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == "*":
            find_head = True
            head_x, head_y = i, j
            heart_x, heart_y = i+1, j
            break

    if find_head:
        break

# 왼쪽 팔
left_arm = 0
for col in range(heart_y-1, -1, -1):
    if graph[heart_x][col] == "*":
        left_arm += 1
    else:
        break
# 오른쪽 팔
right_arm = 0
for col in range(heart_y+1, n):
    if graph[heart_x][col] == "*":
        right_arm += 1
    else:
        break
# 허리
waist = 0
waist_x, waist_y = 0, 0
for row in range(heart_x+1, n):
    if graph[row][heart_y] == "*":
        waist += 1
        waist_x, waist_y = row, heart_y
    else:
        break
# 왼쪽 다리
left_leg = 0
for row in range(waist_x+1, n):
    if graph[row][waist_y-1] == "*":
        left_leg += 1
    else:
        break
# 오른쪽 다리
right_leg = 0
for row in range(waist_x+1, n):
    if graph[row][waist_y+1] == "*":
        right_leg += 1
    else:
        break

print(f"{heart_x+1} {heart_y+1}")  # 심장 위치 (x, y)
print(f"{left_arm} {right_arm} {waist} {left_leg} {right_leg}")  # 왼쪽 팔, 오른쪽 팔, 허리, 왼쪽 다리, 오른쪽 다리의 길이를 공백