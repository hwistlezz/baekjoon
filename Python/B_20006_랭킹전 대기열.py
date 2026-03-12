# 플레이어의 수 p, 방 한개의 정원 m
p, m = map(int, input().split())

rooms = []  # 각 방: [기준 레벨, 남은 자리]
info = []  # 각 방: [(level, nickname), ...]
for _ in range(p):
    level, nickname = input().split()
    level = int(level)

    placed = False

    # 기존 방들 중 먼저 생성된 방부터 확인
    for i in range(len(rooms)):
        base_level, remain = rooms[i]

        # 입장 가능 + 자리 있음
        if (base_level - 10 <= level <= base_level + 10) and remain > 0:
            info[i].append((level, nickname))
            rooms[i][1] -= 1

            placed = True
            break

    # 들어갈 방 없으면 새 방 생성
    if not placed:
        # rooms[i] = (level, 정원)
        rooms.append([level, m - 1])  # 첫 사람 들어갔으니 남은자리 m-1
        info.append([(level, nickname)])  # 리스트 안에 (레벨,닉) 튜플

for i in range(len(rooms)):
    if rooms[i][1] == 0:  # 정원 == 0: 시작된 방
        print("Started!")
    else:  # 대기 중인 방
        print("Waiting!")

    for lv, name in sorted(info[i], key=lambda x: x[1]):  # 닉네임 사전순 출력
        print(lv, name)