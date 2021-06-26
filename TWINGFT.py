# Code Chef Practice (Beginner) Problem
# Birthday Gifts

T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort()

    chefTot = 0
    twinTot = 0

    count = -1
    while K > 0:

        chefTot += A[count]
        if K == 1:
            twinTot += A[count - 1] + A[count - 2]
        else:
            twinTot += A[count - 1]

        K -= 1
        count -= 2

    
    print(max(chefTot, twinTot))
