n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

# x + y + z = k -> x + y = k - z
two_sum = set()  # x + y
for i in range(n):
    for j in range(n):
        a = arr[i] + arr[j]
        two_sum.add(a)

ans = -1
# k - z
for i in range(n-1, -1, -1):
    for j in range(n):
        kz = arr[i] - arr[j]

        if kz in two_sum:
            if arr[i] > ans:
                ans = arr[i]

print(ans)