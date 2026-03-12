# n개 공, k개 바구니
n, k = map(int, input().split())

total_min = k * (k+1) / 2
remain = n - total_min
if total_min > n:
    print(-1)
elif remain % k == 0:
    print(k-1)
else:
    print((k-1) + 1)