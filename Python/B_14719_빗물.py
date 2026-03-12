row, col = map(int, input().split())
blocks = [[False] * col for _ in range(row)]

h = list(map(int, input().split()))
for c in range(col):
    count = 0
    for r in range(row - 1, -1, -1):
        if h[c] > count:
            blocks[r][c] = True
            count += 1
        else:
            continue

rain = 0
for r in range(row-1, -1, -1):
    block_left = False
    count = 0
    for c in range(col):
        # 블럭칸O and 왼쪽 막힘X and 오륵쪽 막힘X -> 왼쪽 막힘O
        if blocks[r][c] and not block_left:
            block_left = True
        # 블럭칸X and 왼쪽 막힘O and 오륵쪽 막힘X -> count++
        elif not blocks[r][c] and block_left:
            count += 1
        # 블럭칸O and 왼쪽 막힘O and 오륵쪽 막힘X -> 오른쪽 막힘, 빗물 생성
        elif blocks[r][c] and block_left:
            rain += count
            count = 0

print(rain)