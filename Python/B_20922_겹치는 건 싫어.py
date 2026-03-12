n, k = map(int, input().split())
arr = list(map(int, input().split()))

cnt = {}
max_len = -1
left = 0

for right in range(n):
    x = arr[right]
    cnt[x] = cnt.get(x, 0) + 1

    # x가 K개 초과하면, 다시 K 이하가 될 때까지 왼쪽을 줄인다
    while cnt[x] > k:
        left_val = arr[left]
        cnt[left_val] -= 1
        left += 1

    max_len = max(max_len, right - left + 1)

print(max_len)