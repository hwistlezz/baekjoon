t = int(input())
for _ in range(t):
    n = int(input())
    team = list(map(int, input().split()))

    # 팀별 참가한 선수 카운트
    runner_count = {}
    for t in team:
        runner_count[t] = runner_count.get(t, 0) + 1

    team_scores = [0] * (n+1)
    score = 1
    nth_runner = {}
    additional_score = [0] * (n+1)
    for t in team:
        if runner_count[t] < 6:  # 6명 미만이면 계산 skip
            continue
        elif runner_count[t] == 6:  # 6명이 참가했으면 점수 추가
            team_scores[t] += score
            nth_runner[t] = nth_runner.get(t, 0) + 1  # 각 팀마다 몇 번째 선수인지 체크

            if nth_runner[t] >= 5:  # 5, 6번째 선수이면 추가 점수 제거
                team_scores[t] -= score
                if nth_runner[t] == 5:  # 5번째 선수는 동점일 때 비교를 위해
                    additional_score[t] += score  # additional_score에 5번째 선수 score 저장

            score += 1  # 1씩 증가

    winner = -1
    min_score = 10**9
    for i in range(1, n+1):
        if team_scores[i] < min_score and team_scores[i] != 0:  # 점수가 1 이상이어야 함!
            min_score = team_scores[i]
            winner = i
        if team_scores[i] == min_score:  # team_scores가 동점이면
            #  5번째 선수 점수(additional_score) 비교
            if additional_score[i] < additional_score[winner]:
                winner = i
            elif additional_score[i] > additional_score[winner]:
                continue

    print(winner)