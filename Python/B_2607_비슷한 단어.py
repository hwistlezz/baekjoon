n = int(input())
words = []
for _ in range(n):
    s = input()
    words.append(s)


def is_similar(s1, s2):
    a = [0] * 26
    b = [0] * 26

    for ch in s1:
        a[ord(ch) - ord('A')] += 1
    for ch in s2:
        b[ord(ch) - ord('A')] += 1

    plus = 0  # s1에 더 많은 문자 수(= s1에서 빼야 함)
    minus = 0  # s2에 더 많은 문자 수(= s1에 더해야 함)

    for i in range(26):
        if a[i] > b[i]:
            plus += a[i] - b[i]
        elif a[i] < b[i]:
            minus += b[i] - a[i]

    # 같은 구성 / 한 글자 추가 / 한 글자 삭제 / 한 글자 교체
    if (
            (plus == 0 and minus == 0) or
            (plus == 0 and minus == 1) or
            (plus == 1 and minus == 0) or
            (plus == 1 and minus == 1)
    ):
        return True

    return False

ans = 0
for i in range(1, n):
    if is_similar(words[0], words[i]):
        ans += 1

print(ans)