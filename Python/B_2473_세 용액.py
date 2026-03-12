import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
x.sort()

best = 3_000_000_001
ans = (0, 0, 0)

for i in range(n-2):  # n-3까지
    left = i + 1
    right = n - 1

    while left < right:
        s = x[i] + x[left] + x[right]

        if abs(s) < best:
            best = abs(s)
            ans = (x[i], x[left], x[right])
            if best == 0:
                break

        if s > 0:
            right -= 1
        elif s < 0:
            left += 1
        else:
            break

    if best == 0:
        break

print(*ans)