n = int(input())

ingredients = []
for _ in range(n):
    # 신맛 s, 쓴맛 b / 음식의 신맛은 사용한 재료의 신맛의 곱, 쓴맛은 합
    s, b = map(int, input().split())
    ingredients.append((s, b))

ans = 10**9

# 1. 비트마스킹 풀이
for mask in range(1, 1 << n):  # 범위는 1부터(공집합(0) 제외) ~ (2^n - 1) 까지
    s_prod = 1
    b_sum = 0

    for i in range(n):
        if mask & (1 << i):  # # i번째 비트가 1인지
            s, b = ingredients[i]
            s_prod *= s
            b_sum += b

    ans = min(ans, abs(s_prod - b_sum))

print(ans)


# 2. 백트래킹 풀이
# def dfs(i, s_prod, b_sum, used):
#     global ans
#
#     if i == n:
#         if used:
#             ans = min(ans, abs(s_prod - b_sum))
#
#         return
#
#     # 1) i번째 재료 사용
#     s, b = ingredients[i]
#     dfs(i+1, s_prod * s, b_sum + b, True)
#
#     # 2) i번째 재료 미사용
#     dfs(i+1, s_prod, b_sum, used)
#
#
# dfs(0, 1, 0, False)
# print(ans)