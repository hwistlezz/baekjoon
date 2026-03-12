while True:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        break

    tri = [a, b, c]
    A = max(tri)
    tri.remove(A)
    B = max(tri)
    C = min(tri)

    if A >= B+C:
        print("Invalid")
        continue
    elif A == B and A == C:
        print("Equilateral")
        continue
    elif A == B or B == C or C == A:
        print("Isosceles")
        continue
    elif A != B and B != C and C != A:
        print("Scalene")
        continue