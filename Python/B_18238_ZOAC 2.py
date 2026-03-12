s = input()

cur = 0
ans = 0

for ch in s:
    nxt = ord(ch) - ord('A')
    d = abs(nxt - cur)
    ans += min(d, 26 - d)
    cur = nxt

print(ans)