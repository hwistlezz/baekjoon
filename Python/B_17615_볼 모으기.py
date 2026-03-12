n = int(input())
s = input()

balls = []
ball_cnt = {}

for color in s:
    balls.append(color)
    ball_cnt[color] = ball_cnt.get(color, 0) + 1

# 하나가 0개이면 종료
if ball_cnt.get('R', 0 ) == 0 or ball_cnt.get('B', 0 ) == 0:
    print(0)
    exit()

# 왼쪽 연속 개수
left_r = 0
for i in range(n):
    if balls[i] == 'R':
        left_r += 1
    else:
        break

left_b = 0
for i in range(n):
    if balls[i] == 'B':
        left_b += 1
    else:
        break

# 오른쪽 연속 개수
right_r = 0
for i in range(n-1, -1, -1):
    if balls[i] == 'R':
        right_r += 1
    else:
        break

right_b = 0
for i in range(n-1, -1, -1):
    if balls[i] == 'B':
        right_b += 1
    else:
        break


ans = min(
    ball_cnt['R'] - left_r,     # R을 왼쪽으로
    ball_cnt['R'] - right_r,    # R을 오른쪽으로
    ball_cnt['B'] - left_b,     # B를 왼쪽으로
    ball_cnt['B'] - right_b,    # B를 오른쪽으로
)
print(ans)