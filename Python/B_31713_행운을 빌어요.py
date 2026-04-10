t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    ans = 0

    # 잎의 개수(b)가 현재 줄기(a)로 수용할 수 있는 최대치보다, 많으면 줄기 추가
    while a * 4 < b:
        a += 1
        ans += 1

    # 현재 줄기(a)를 채우기 위한 최소 잎의 개수보다, 가진 잎(b)이 적으면 잎 추가
    if 3 * a > b:
        ans += 3 * a - b

    print(ans)