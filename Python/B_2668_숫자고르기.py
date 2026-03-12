N = int(input())

second = [0] + [int(input()) for _ in range(N)]

visited = [False] * (N+1)
ans = []


def dfs(start):
    global ans
    path = []  # 방문 순서(노드 번호)
    pos = {}  # 이번 DFS(탐색) 경로에서, 각 노드가 몇 번째로 등장했는지 (pos[node] = path에서의 인덱스)

    cur = start
    while True:
        # 이미 결론 난 노드를 만나면 종료
        if visited[cur]:
            break

        # 이번 경로에서 다시 만나면 사이클 발생
        if cur in pos:
            cycle_start = pos[cur]  # 사이클 시작하는 index
            ans.extend(path[cycle_start:])  # extend(iterable) -> 여러 요소를 하나씩 풀어서 추가
            break

        # 경로 기록
        pos[cur] = len(path)  # pos[node] = path에서의 인덱스
        path.append(cur)
        cur = second[cur]

    for p in path:
        visited[p] = True


for i in range(1, N+1):
    dfs(i)

ans = sorted(set(ans))
print(len(ans))  # 뽑힌 정수들의 개수
# 뽑힌 정수들을 작은 수부터 큰 수의 순서로 한 줄에 하나씩 출력
for x in ans:
    print(x)