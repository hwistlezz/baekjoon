n = int(input())

pillars = []
max_h = -1
for _ in range(n):
    l, h = map(int, input().split())
    pillars.append((l, h))

    max_h = max(max_h, h)

pillars.sort()

max_start_x = -1
max_start_idx = -1
for i in range(len(pillars)):
    if pillars[i][1] == max_h:
        max_start_x = pillars[i][0]
        max_start_idx = i
        break

max_end_x = -1
max_end_idx = -1
for i in range(len(pillars)):
    if pillars[i][1] == max_h:
        max_end_x = pillars[i][0] + 1
        max_end_idx = i

area = 0
x = pillars[0][0]
h = pillars[0][1]
for i in range(1, max_start_idx+1):  # max_h 왼쪽 영역
    cur_x, cur_h = pillars[i]
    if h <= cur_h:
        area += abs(cur_x - x) * h
        x = cur_x
        h = cur_h

x = pillars[-1][0] + 1
h = pillars[-1][1]
for i in range(n-2, max_end_idx-1, -1):  # max_h 오른쪽 영역
    cur_x, cur_h = pillars[i]
    if h <= cur_h:
        area += abs((cur_x + 1) - x) * h
        x = pillars[i][0] + 1
        h = pillars[i][1]

area += (pillars[max_end_idx][0] - pillars[max_start_idx][0] + 1) * max_h

print(area)