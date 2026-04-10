from decimal import Decimal, ROUND_HALF_UP

words = input()

ph = 0
pg = 0

ph += words.count('H')
ph += words.count('A')
ph += words.count('P')
ph += words.count('Y')

pg += words.count('S')
pg += words.count('A')
pg += words.count('D')

if ph == 0 and pg == 0:
    print("50.00")
else:
    # 1. 분자와 분모를 모두 Decimal 객체로 변환하여 정확한 소수 연산을 수행
    h = Decimal(ph) / Decimal(ph + pg) * Decimal(100)
    # 2. quantize()와 ROUND_HALF_UP을 사용하여 소수점 둘째 자리까지 사사오입
    result = h.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    print(result)