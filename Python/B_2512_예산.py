n = int(input())
need_budget = list(map(int, input().split()))
total_budget = int(input())

if sum(need_budget) <= total_budget:
    print(max(need_budget))
else:
    low, high = 0, max(need_budget),
    ans = 0
    while low <= high:
        mid = (low + high) // 2

        if sum(min(mid, x) for x in need_budget) <= total_budget:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    print(ans)



# if sum(need_budget) <= total_budget:
#     print(max(need_budget))
# else:
#     cnt = len(need_budget)
#     division = total_budget // cnt
#     need_budget.sort()
#
#     for i in range(cnt):
#         if need_budget[i] <= division:
#             total_budget -= need_budget[i]
#             division = total_budget // (cnt - (i+1))
#         else:
#             print(division)
#             break