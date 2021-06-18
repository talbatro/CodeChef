# Code Chef Practice (Beginner) Problem
# Hoop Jump

T = int(input()) # input test cases amount

for t in range(T): # iterate over each test case

    N = int(input()) # input number as integer

    L = (N + 1) / 2 # last hoop to be jumped in

    print(int(L)) # print out result
