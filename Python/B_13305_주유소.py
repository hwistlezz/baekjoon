n = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))

price_copy = price[:n-1]
min_price = min(price_copy)
less_price = 10**9
total_cost = 0
for i in range(n-1):
    if price[i] == min_price:
        total_cost += price[i] * sum(length[i:n-1])
        break
    elif price[i] < less_price:
        less_price = price[i]
        total_cost += length[i] * less_price
    else:  # price[i] >= less_price
        total_cost += length[i] * less_price

print(total_cost)