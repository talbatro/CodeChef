# Code Chef Practice (Beginner) Problem
# Chef and SnackDown

T = int(input())

for t in range(T):

    A,B = map(int, input().split())

    if A > B:
        print(">")
    elif A < B:
        print("<")
    else:
        print("=")
