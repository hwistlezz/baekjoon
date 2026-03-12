import sys
input = sys.stdin.readline

n, dish, k, coupon = map(int, input().split())
sushi = []
for _ in range(n):
    x = int(input())
    sushi.append(x)

cnt = [0] * (dish + 1)
typ = 0

# 1) 초기 윈도우 [0 ~ k-1]
for i in range(k):
    x = sushi[i]
    if cnt[x] == 0:
        typ += 1

    cnt[x] += 1

ans = typ + (1 if cnt[coupon] == 0 else 0)

# 2) 윈도우를 1칸씩 N-1번 이동 (총 N개 구간을 보게 됨)
for left in range(1, n):
    out = sushi[left - 1]
    cnt[out] -= 1
    if cnt[out] == 0:
        typ -= 1

    inn = sushi[(left + k - 1) % n]
    if cnt[inn] == 0:
        typ += 1

    cnt[inn] += 1

    cur = typ + (1 if cnt[coupon] == 0 else 0)
    ans = max(ans, cur)

print(ans)