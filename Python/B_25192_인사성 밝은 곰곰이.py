n = int(input())
ans = 0
for _ in range(n):
    chat = input()

    if chat == "ENTER":
        user = {}
        continue
    else:
        user[chat] = user.get(chat, 0) + 1

        if user[chat] > 1:
            continue
        else:
            ans += 1

print(ans)