t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))

    sum = 0
    even_min = 101
    for n in nums:
        if n % 2 == 0:
            sum += n

            if n < even_min:
                even_min = n



    print(f"{sum} {even_min}")