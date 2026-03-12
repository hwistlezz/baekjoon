m, n = map(int, input().split())
length = list(map(int, input().split()))


def can_make(x):
    total = 0
    for l in length:
        total += l // x

    return total >= m


low = 1
high = max(length)
ans = 0
while low <= high:
    mid = (low + high) // 2

    if can_make(mid):
        low = mid + 1
        ans = mid
    else:
        high = mid - 1

print(ans)