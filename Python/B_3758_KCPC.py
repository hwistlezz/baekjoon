t = int(input())
for _ in range(t):
    # 팀의 개수 n, 문제의 개수 k, 당신 팀의 ID t, 로그 엔트리의 개수 m
    n, k, my_team, m = map(int, input().split())

    # scores[team][problem]: n팀의 k번 문제에서 얻은 최고점
    scores = [[0] * (k + 1) for _ in range(n + 1)]
    # submit_cnt[team]: 팀당 총 제출 횟수
    submit_cnt = [0] * (n+1)
    # last_submit[team]: 마지막 제출 시간 체크
    last_submit = [0] * (n+1)

    count = 1
    for m in range(m):
        # 팀 ID i, 문제 번호 j, 획득한 점수 s
        i, j, s = map(int, input().split())

        scores[i][j] = max(scores[i][j], s)
        submit_cnt[i] += 1
        last_submit[i] = count

        count += 1

    total_score = [0] * (n+1)
    for team in range(n+1):
        for problem in range(k+1):
            total_score[team] += scores[team][problem]

    my_score = total_score[my_team]
    my_ranking = 1
    for i in range(n+1):
        if i == my_team:
            continue

        if my_score > total_score[i]:
            continue
        elif my_score < total_score[i]:
            my_ranking += 1
        else:  # 총점이 같으면
            # 최종 점수가 같은 경우, 풀이를 제출한 횟수가 적은 팀의 순위가 높다.
            if submit_cnt[my_team] > submit_cnt[i]:
                my_ranking += 1
            elif submit_cnt[my_team] < submit_cnt[i]:
                continue
            else:  # 최종 점수도 같고 제출 횟수도 같은 경우, 마지막 제출 시간이 더 빠른 팀의 순위가 높다.
                if last_submit[my_team] > last_submit[i]:
                    my_ranking += 1
                elif last_submit[my_team] < last_submit[i]:
                    continue
    # 당신 팀의 순위 출력
    print(my_ranking)