n, k = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0


def merge(arr, p, q, r):
    global cnt
    i, j = p, q+1
    temp = []
    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    # 왼쪽 배열이 남은 경우
    while i <= q:
        temp.append(arr[i])
        i += 1
    # 오른쪽 배열이 남은 경우
    while j <= r:
        temp.append(arr[j])
        j += 1
    # 결과를 arr에 저장
    i, t = p, 0
    while i <= r:
        arr[i] = temp[t]
        cnt += 1
        if cnt == k:
            print(arr[i])
            return

        i += 1
        t += 1

def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)


merge_sort(arr, 0, n-1)
if cnt < k:
    print(-1)