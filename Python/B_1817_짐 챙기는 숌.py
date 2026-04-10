n, max_box_weight = map(int, input().split())

if n == 0:
    print(0)
    exit()

books = list(map(int, input().split()))

cnt = 1
cur_box_weight = 0
for book in books:
    if cur_box_weight + book <= max_box_weight:
        cur_box_weight += book
    else:
        cnt += 1
        cur_box_weight = book

print(cnt)