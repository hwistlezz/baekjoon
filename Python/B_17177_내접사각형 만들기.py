import math
a, b, c = map(int, input().split())

# a는 지름 -> 원의 지름을 빗변으로 하는 직각삼각형 2개
diagonal1_sqrt = a*a - b*b
diagonal2_sqrt = a*a - c*c

if diagonal1_sqrt < 0 or diagonal2_sqrt < 0:
    print(-1)
else:
    diagonal1 = math.sqrt(diagonal1_sqrt)
    diagonal2 = math.sqrt(diagonal2_sqrt)

    # 프톨레마이오스 정리 이용
    # a * x + b * c == diagonal1 * diagonal2
    x = (diagonal1 * diagonal2 - b * c) / a

    if x <= 0:
        print(-1)
    else:
        print(round(x))