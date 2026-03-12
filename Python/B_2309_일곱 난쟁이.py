heights = [int(input()) for _ in range(9)]

total = sum(heights)
find = False
for i in range(9):
    for j in range(i+1, 9):
        if total - heights[i] - heights[j] == 100:
            fake1, fake2 = heights[i], heights[j]
            find = True
            break

    if find:
        break

heights.sort()
for h in heights:
    if h != fake1 and h != fake2:
        print(h)