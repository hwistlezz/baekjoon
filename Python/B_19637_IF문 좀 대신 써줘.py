import sys
input = sys.stdin.readline

n, m = map(int, input().split())

names = []
limits = []
for _ in range(n):
    name, limit = input().split()
    names.append(name)
    limits.append(int(limit))


# target 이상(>=)이 처음 등장하는 위치(idx)
def lower_bound(arr, target):
    # 탐색 범위 = [left, right)
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left


for _ in range(m):
    power = int(input())
    print(names[lower_bound(limits, power)])