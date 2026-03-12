n = int(input())
w = list(map(int, input().split()))
w.sort()

w_sum = []
for i in range(n):  # 0, 2n-1 / 1, 2n-2 / ... / n-1, n
    x = w[i] + w[2*n - i - 1]
    w_sum.append(x)

ans = min(w_sum)
print(ans)