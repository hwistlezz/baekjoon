s = input()
t = input()

s_len = len(s)
goal = s

# 시간 초과
# s -> t
# def process(s, t):
#     if len(s) == len(t):
#         if s == t:
#             return True
#         else:
#             return False
#
#     # 1) 뒤에 'A' 추가
#     s1 = s + 'A'
#     result1 = process(s1, t)
#
#     # 2) 뒤에 'B' 추가 후 뒤집기
#     s2 = s + 'B'
#     s2 = s2[::-1]
#     result2 = process(s2, t)
#
#     return result1 or result2


# t -> s
def process(s):
    if len(s) == s_len:
        if s == goal:
            return True
        else:
            return False

    result1 = False
    result2 = False

    if s[-1] == 'A':  # 1) 뒤에서 'A' 제거
        s1 = s[:-1]
        result1 = process(s1)

    if s[0] == 'B':  # 2) 뒤집은 후 뒤에서 'B' 제거
        s2 = s[::-1]
        s2 = s2[:-1]
        result2 = process(s2)

    return result1 or result2

if process(t):
    print(1)
else:
    print(0)