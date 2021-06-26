# Code Chef Practice (Beginner) Problem
# Tom and Jerry 1

T = int(input())

for t in range(T):
    a,b,c,d,K = map(int, input().split())

    xDif = abs(c-a)
    yDif = abs(d-b)
    total = xDif + yDif

    if K < total:
        print("NO")
        continue

    if (K - total) % 2 == 0:
        print("YES")
    else:
        print("NO")
