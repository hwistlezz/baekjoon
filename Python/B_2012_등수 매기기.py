import sys
input = sys.stdin.readline

n = int(input())

scores = []
for _ in range(n):
    x = int(input())
    scores.append(x)

scores.sort()
total = 0
for i in range(n):
    total += abs((i+1) - scores[i])

print(total)