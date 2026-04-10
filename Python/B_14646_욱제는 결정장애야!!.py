n = int(input())
menu = list(map(int, input().split()))
check = [False] * (n+1)
cnt = 0
ans = 0

for m in menu:
    if not check[m]:
        check[m] = True
        cnt += 1
    else:
        cnt -= 1

    ans = max(ans, cnt)

print(ans)