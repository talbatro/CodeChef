# Code Chef Practice (Beginner) Problem
# Chef and SnackDown

T = int(input())

for t in range(T):

    N = int(input())

    years = [2010, 2015, 2016, 2017, 2019]

    if N in years:
        print("HOSTED")
    else:
        print("NOT HOSTED")
