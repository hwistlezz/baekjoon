n = int(input())  # 굴다리 길이
m = int(input())  # 가로등 개수
pos = list(map(int, input().split()))


def can_cover(h):
    # 1) 시작(0) 커버
    if pos[0] - h > 0:
        return False

    # 2) 끝(N) 커버
    if pos[-1] + h < n:
        return False

    # 3) 중간 gap 커버 (가로등 사이 거리 <= 2h)
    for i in range(m-1):
        if pos[i+1] - pos[i] > (2 * h):
            return False

    return True


low, high = 0, n
ans = n
while low <= high:
    mid = (low + high) // 2

    if can_cover(mid):
        ans = mid
        high = mid - 1  # 더 작은 답이 있는지 왼쪽 탐색
    else:
        low = mid + 1  # 불가능 → 오른쪽 탐색

print(ans)