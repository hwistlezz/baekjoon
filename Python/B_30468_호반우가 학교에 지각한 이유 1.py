s, d, i, l, n = map(int, input().split())

x = 4*n - (s + d + i + l)

if x < 0:
    print(0)
else:
    print(x)