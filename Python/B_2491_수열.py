n = int(input())
arr = list(map(int, input().split()))

ans = 1
inc = 1
dec = 1
for i in range(n-1):
    if arr[i] <= arr[i+1]:
        inc += 1
    else:
        inc = 1

    if arr[i] >= arr[i+1]:
        dec += 1
    else:
        dec = 1

    ans = max(ans, inc, dec)

print(ans)