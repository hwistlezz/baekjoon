import sys
input = sys.stdin.readline
n, m = map(int, input().split())
# keywords = [input() for _ in range(n)]
# used = [input().split(',') for _ in range(m)]

# keywords = set()
# for i in range(n):
#     x = input()
#     keywords.add(x)
#
# used = set()
# for i in range(m):
#     words = input().split(',')
#
#     for w in words:
#         used.add(w)
#
#     print(len(keywords - used))

# -> 시간 초과
# 자료구조(list vs set) 때문에 연산 비용이 O(N) ↔ O(1)로 갈린 것

keywords = set()
for _ in range(n):
    x = input().strip()
    keywords.add(x)

remain = len(keywords)

for i in range(m):
    used = input().strip().split(',')

    for x in used:
        if x in keywords:
            keywords.discard(x)
            remain -= 1

    print(remain)