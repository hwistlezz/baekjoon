x, y = map(int, input().split())
z = (y * 100) // x

if z >= 99:
    print(-1)
else:
    lo, hi = 1, 1_000_000_000
    ans = -1

    while lo <= hi:
        mid = (lo + hi) // 2
        newZ = (100 * (y + mid)) // (x + mid)

        if newZ > z:
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1

    print(ans)

# if z >= 99:
#     print(-1)
# else:
#     t = z + 1
#     numer = (t * x) - 100 * y
#     denom = 100 - t
#
#     ans = (numer + denom - 1) // denom
#     print(ans)