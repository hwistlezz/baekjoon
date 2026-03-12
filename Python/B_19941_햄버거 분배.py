# 식탁 길이 n, 햄버거 선택 거리 k
n, k = map(int, input().split())
pos = input()

eaten_burger = [False] * n
eaten_cnt = 0
for idx in range(len(pos)):
    if pos[idx] == 'P':
        for i in range(max(0, (idx-k)), min((idx+k)+1, n)):
            if pos[i] == 'H' and not eaten_burger[i]:
                eaten_burger[i] = True
                eaten_cnt += 1
                break

print(eaten_cnt)