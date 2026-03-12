n, x = map(int, input().split())
visit = list(map(int, input().split()))

max_visit = -1
period_count = 0

# 시간 초과
# for i in range(0, n-x):
#     partial_count = visit[i]
#
#     for j in range(1, x):
#         partial_count += visit[i+j]
#
#     if partial_count == max_visit:
#         period_count += 1
#     elif partial_count > max_visit:
#         period_count = 1
#         max_visit = partial_count

# -> 슬라이딩 윈도우 방법 사용
partial_count = sum(visit[:x])
if partial_count > max_visit:
    max_visit = partial_count
    period_count = 1

for i in range(n-x):
    partial_count -= visit[i]
    partial_count += visit[i+x]

    if partial_count > max_visit:
        max_visit = partial_count
        period_count = 1
    elif partial_count == max_visit:
        period_count += 1

if max_visit == 0:
    print("SAD")
else:
    print(max_visit)
    print(period_count)