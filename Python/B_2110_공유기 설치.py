import sys
input = sys.stdin.readline

n, c = map(int, input().split())

houses = []
for _ in range(n):
    x = int(input())
    houses.append(x)

houses.sort()


def install_check(m):
    count = 1
    # 마지막 설치 위치: last
    last = houses[0]

    for i in range(1, n):
        if (houses[i] - last) >= m:
            count += 1
            last = houses[i]

        if count >= c:
            return True

    return False


l = 1
r = houses[n-1] - houses[0]  # 거리의 최대값(좌표값 아님!)
ans = 0
while l < r:
    m = (l + r + 1) // 2

    if install_check(m):  # 가능하면 더 키워본다
        l = m
    else:  # 불가능하면 줄인다
        r = m-1

print(l)  # l == r == 최대 가능한 거리