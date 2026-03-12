import sys
input = sys.stdin.readline

N, game = input().split()
N = int(N)

names = set()
for _ in range(N):
    name = input().strip()
    names.add(name)

need = {"Y" : 1, "F" : 2, "O": 3}[game]
ans = len(names) // need

print(ans)