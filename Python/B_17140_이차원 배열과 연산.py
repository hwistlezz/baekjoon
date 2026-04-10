r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]


def sort_line(line):
    # 1) 0 제거
    line = [x for x in line if x != 0]

    # 2) 숫자 개수 세기
    cnt = {}
    for x in line:
        cnt[x] = cnt.get(x, 0) + 1

    # 3) 정렬용 리스트 만들기 -> (숫자, 개수) -> 1. 개수 오름차순  2. 숫자 오름차순
    pairs = list(cnt.items())  # [(숫자, 개수), (숫자, 개수), ...]
    pairs.sort(key=lambda x : (x[1], x[0]))

    # 4) 다시 펼치기
    new_line = []
    for num, count in pairs:
        new_line.append(num)
        new_line.append(count)

    return new_line


def operate_R(arr):
    new_A = []
    max_len = 0

    for row in arr:
        new_row = sort_line(row)[:100]
        new_A.append(new_row)
        max_len = max(max_len, len(new_row))

    for row in new_A:
        row += [0] * (max_len - len(row))

    return new_A


def operate_C(arr):
    # 전치(transpose) 이용해서 R처럼 처리 후 다시 전치
    # 1) A를 전치 (열을 행으로 변환)
    transposed = list(map(list, zip(*arr)))

    # 2) R 연산처럼 처리
    transposed = operate_R(transposed)

    # 3) 다시 전치해서 행렬로 돌리기
    new_A = list(map(list, zip(*transposed)))

    return new_A


time = 0

while time <= 100:
    if 0 <= r-1 < len(A) and 0 <= c-1 < len(A[0]):
        if A[r-1][c-1] == k:
            print(time)
            break

    if time == 100:
        print(-1)
        break

    row_len = len(A)
    col_len = len(A[0])

    if row_len >= col_len:  # R 연산
        A = operate_R(A)
    else:  # C 연산
        A = operate_C(A)


    time += 1