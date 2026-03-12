from collections import deque

n, k = map(int, input().split())
durability = deque(map(int, input().split()))
have_robot = deque([False] * (2*n))


zero_count = 0
process_count = 0
while zero_count < k:  # 내구도 0인 칸의 개수가 k 이상이면 종료
    process_count += 1

    # 1) 벨트 1칸 회전(이동) (로봇도 같이)
    durability.rotate(1)
    have_robot.rotate(1)
    # 내리는 위치(n 칸) -> 로봇 내리기
    have_robot[n-1] = False

    # 2) 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 1칸 이동할 수 있다면 이동
    for i in range(n-2, -1, -1):  # (n-1)부터 1 까지 역순(먼저 올라온 로봇순으로)
        # 이동 전에 로봇이 있고
        # 이동하려는 칸에 로봇이 없으며,
        # 그 칸의 내구도가 1 이상 남아 있어야 함
        # 만약 이동할 수 없다면 가만히 있는다.
        if have_robot[i] and not have_robot[i+1] and durability[i+1] >= 1:
            have_robot[i] = False
            have_robot[i+1] = True

            durability[i+1] -= 1

            # 내구도 0되면 zero_count++
            if durability[i+1] == 0:
                zero_count += 1

    # 내리는 위치(n 칸) -> 로봇 내리기
    have_robot[n - 1] = False

    # 3) 올리는 위치(1번 칸)에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if not have_robot[0] and durability[0] >= 1:
        have_robot[0] = True

        durability[0] -= 1

        # 내구도 0되면 zero_count++
        if durability[0] == 0:
            zero_count += 1

print(process_count)