s = input()
n = len(s)
a_count = s.count('a')

if a_count == 0 or a_count == n:
    print(0)
else:
    s2 = s + s

    a_max = 0
    for i in range(n):
        a_max = max(a_max, s2[i:i+a_count].count('a'))

    need = a_count - a_max
    print(need)