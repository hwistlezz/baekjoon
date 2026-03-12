start, target = map(int, input().split())
n = int(input())
bookmarks = [int(input()) for _ in range(n)]
bookmarks.sort()

if target in bookmarks:
    print(1)
    exit()

best = start
ans = abs(target - best)
for x in bookmarks:
    if abs(target - x) < abs(target - best):
        best = x
        ans = 1 + abs(target - best)

print(ans)