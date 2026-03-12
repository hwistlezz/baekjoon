import sys
input = sys.stdin.readline

s = input().rstrip()
m = int(input())

# 커서를 기준으로 “왼쪽/오른쪽”을 따로 stack으로 관리
left = list(s)  # 커서 왼쪽
right = []      # 커서 오른쪽

for _ in range(m):
    cmd = input().rstrip()

    if cmd[0] == 'L':
        if left:
            right.append(left.pop())
    elif cmd[0] == 'D':
        if right:
            left.append(right.pop())
    elif cmd[0] == 'B':
        if left:
            left.pop()
    else:
        left.append(cmd[2])

sys.stdout.write(''.join(left + right[::-1]))