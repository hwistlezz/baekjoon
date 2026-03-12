def dfs(n, pos, expr):
    # 종료 조건
    if pos == n+1:
        if calculate(expr) == 0:
            print(expr)

        return

    for op in [" ", "+", "-"]:
        dfs(n, pos+1, expr+op+str(pos))


def calculate(expr):
    ex = expr.replace(" ", "")

    total = 0  # 지금까지 확정된 합
    sign = 1  # 현재 숫자 앞의 부호 (+1 또는 -1)
    cur = 0  # 현재 읽고 있는 숫자
    for x in ex:
        if x.isdigit():  # 숫자면
            cur = (cur * 10) + int(x)
        else:
            if x == "+":
                total += (sign * cur)
                cur = 0
                sign = 1
            elif x == "-":
                total += (sign * cur)
                cur = 0
                sign = -1

    total += (sign * cur)  # 마지막 숫자 처리
    return total



t = int(input())
for _ in range(t):
    n = int(input())

    dfs(n, 2, "1")
    print()