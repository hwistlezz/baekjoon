t = int(input())
for _ in range(t):
    n = int(input())

    total = 0
    most = 0
    no_winner = False
    R = -1
    for i in range(n):
        x = int(input())
        total += x

        if most == x:
            no_winner = True

        if x > most:
            most = x
            R = i+1
            no_winner = False

    if no_winner:
        print("no winner")
    elif most / total > 0.5:
        print(f"majority winner {R}")
    else:
        print(f"minority winner {R}")