n = int(input())
ex = input()

nums = []
ops = []
for i in range(n):
    if i % 2 == 0:
        nums.append(int(ex[i]))
    else:
        ops.append(ex[i])


def calc(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b


def dfs(idx, cur_val):
    global ans
    if idx >= len(ops):
        ans = max(ans, cur_val)
        return

    # 1) 괄호 사용 X: 현재값과 다음 숫자를 바로 계산
    nxt_val = calc(cur_val, ops[idx], nums[idx+1])
    dfs(idx+1, nxt_val)

    # 2) 괄호 사용 O: 다음 연산을 먼저 계산
    if (idx + 1) < len(ops):
        temp = calc(nums[idx+1], ops[idx+1], nums[idx+2])
        dfs(idx+2, calc(cur_val, ops[idx], temp))


ans = -float('inf')
dfs(0, nums[0])
print(ans)
