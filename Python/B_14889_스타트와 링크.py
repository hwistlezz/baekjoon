N = int(input())
stat = [list(map(int, input().split())) for _ in range(N)]

ans = 10**9
selected = [False] * N


def cal_team_stat(team_list):
    team_stat = 0
    for i in team_list:
        for j in team_list:
            if i == j:
                continue
            else:
                team_stat += stat[i][j]

    return team_stat


def backtracking(idx, picked):
    global ans
    if picked == N // 2:
        start_list = []
        link_list = []

        for i in range(N):
            if selected[i]:
                start_list.append(i)
            else:
                link_list.append(i)

        start_team_stat = cal_team_stat(start_list)
        link_team_stat = cal_team_stat(link_list)

        ans = min(ans, abs(start_team_stat - link_team_stat))
        return

    if idx == N:  # 더 이상 팀을 완성할 수 없으니 종료
        return

    # idx번째 사람을 선택하거나 / 선택하지 않거나
    selected[idx] = True
    backtracking(idx+1, picked+1)

    selected[idx] = False
    backtracking(idx+1, picked)


backtracking(0, 0)
print(ans)