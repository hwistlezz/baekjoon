n, m = map(int, input().split())
cards = []
for i in range(n):
    card = list(map(int, input().split()))
    card.sort(reverse=True)
    cards.append(card)

scores = [0] * n
for i in range(m):
    max_num = -1
    win_player = []

    for j in range(n):
        if cards[j][i] > max_num:
            max_num = cards[j][i]
            win_player = []
            win_player.append(j)
        elif cards[j][i] == max_num:
            win_player.append(j)

    for p in win_player:
        scores[p] += 1

winner = []
max_scores = -1
for i in range(n):
    if scores[i] > max_scores:
        max_scores = scores[i]
        winner = []
        winner.append(i+1)
    elif scores[i] == max_scores:
        winner.append(i+1)

print(*winner)