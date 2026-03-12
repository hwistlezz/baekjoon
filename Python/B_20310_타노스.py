s = input()
cnt = {}
for num in s:
    cnt[num] = cnt.get(num, 0) + 1

remove0 = cnt.get('0', 0) // 2
remove1 = cnt.get('1', 0) // 2

n = len(s)
result = []
# 1은 앞에서부터 지운다
for i in range(n):
    if s[i] == '1' and remove1 > 0:
        remove1 -= 1
    else:
        result.append(s[i])

# 0은 뒤에서부터 지운다
m = len(result)
ans = []
for i in range(m-1, -1, -1):
    if result[i] == '0' and remove0 > 0:
        remove0 -= 1
    else:
        ans.append(result[i])

print(''.join(reversed(ans)))