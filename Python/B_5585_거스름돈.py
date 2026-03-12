n = int(input())
x = 1000 - n

cnt = 0
while x >= 500:
    x -= 500
    cnt += 1

while x >= 100:
    x -= 100
    cnt += 1

while x >= 50:
    x -= 50
    cnt += 1

while x >= 10:
    x -= 10
    cnt += 1

while x >= 5:
    x -= 5
    cnt += 1

while x >= 1:
    x -= 1
    cnt += 1

print(cnt)