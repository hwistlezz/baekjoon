n = int(input())
x = list(map(int, input().split()))

left = 0
right = n-1

best = abs(x[left] + x[right])
ans = (x[left], x[right])

while left < right:
    temp = x[left] + x[right]

    # 1) 최적 갱신은 "절댓값" 기준 + ans도 같이 갱신
    if abs(temp) < best:
        best = abs(temp)
        ans = (x[left], x[right])

    # 2) 포인터 이동
    if temp > 0:
        right -= 1
    elif temp < 0:
        left += 1
    else:  # temp == 0
        break

print(*ans)