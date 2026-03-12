num = [int(input()) for _ in range(9)]
total = sum(num)

found = False
for i in range(9):
    for j in range(i+1, 9):
        if total - num[i] - num[j] == 100:
            fake1, fake2 = num[i], num[j]
            found = True
            break

    if found:
        break

for x in num:
    if x != fake1 and x != fake2:
        print(x)