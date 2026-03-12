import heapq
from collections import deque
import sys
input = sys.stdin.readline
# n개의 주차 공간, m대의 차량
n, m = map(int, input().split())
fee = [0] + list(int(input()) for _ in range(n))
weight = [0] + list(int(input()) for _ in range(m))

empty_space = []  # 주차 가능한 공간
for i in range(1, n+1):
    empty_space.append(i)
heapq.heapify(empty_space)

now_parking = {}  # (현재 주차 중인 차, 주차 중인 공간)
waiting = deque()  # 주차 공간 없어서 대기하는 차들
total_fee = 0

for _ in range(2*m):
    car_num = int(input())

    if car_num > 0:  # 차가 들어옴
        if empty_space:  # 주차 공간 남아 있으면
            spot_num = heapq.heappop(empty_space)  # 가장 작은 번호 할당
            now_parking[car_num] = spot_num

            total_fee += fee[spot_num] * weight[car_num]  # 요금 계산
        else:  # 주차 공간 없으면
            waiting.append(car_num)
    else:  # 차가 나감
        car_num *= -1
        spot_num = now_parking.pop(car_num)  # 나갈 차의 주자 공간 번호 (주차 중인 차 빼기)
        heapq.heappush(empty_space, spot_num)  # 차 뺀 공간을, 다시 주차 가능으로 변경

        if waiting:  # 차 나간 후, 대기 중인 차가 있으면
            car_num2 = waiting.popleft()  # 가장 오래 기다린 차
            spot_num2 = heapq.heappop(empty_space)  # 남은 공간 중에 번호 가장 작은 공간 할당
            now_parking[car_num2] = spot_num2

            total_fee += fee[spot_num2] * weight[car_num2]

print(total_fee)