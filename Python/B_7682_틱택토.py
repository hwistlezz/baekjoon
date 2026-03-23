while True:
    game = input()
    if game == "end":
        break

    cnt = {}
    for k in game:
        cnt[k] = cnt.get(k, 0) + 1

    # 개수 안 맞은 경우
    if cnt.get('X', 0) - cnt.get('O', 0) > 1 or cnt.get('X', 0) < cnt.get('O', 0):
        print("invalid")
        continue

    # 게임 끝났는데, 더 진행한 경우
    lines = [
        # 가로
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        # 세로
        (0, 3, 6), (1, 4 ,7), (2, 5, 8),
        # 대각선
        (0, 4, 8), (2, 4, 6)
    ]

    x_win, o_win = False, False
    for a, b, c in lines:
        if game[a] == game[b] == game[c] == 'X':
            x_win = True
        elif game[a] == game[b] == game[c] == 'O':
            o_win = True

    if x_win and o_win:
        print("invalid")
        continue

    if x_win and cnt.get('X', 0) - cnt.get('O', 0) == 1:
        print("valid")
        continue
    if o_win and cnt.get('X', 0) - cnt.get('O', 0) == 0:
        print("valid")
        continue

    if not x_win and not o_win:
        if cnt.get('X', 0) - cnt.get('O', 0) == 1 and cnt.get('.', 0) == 0:
            print("valid")
            continue

    print("invalid")