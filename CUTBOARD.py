# Code Chef Practice (Beginner) Problem
# Cut the Board

T = int(input()) # input test cases amount

for t in range(T): # iterate over each test case

    N, M = map(int, input().split()) # input numbers as integer

    total = (N - 1) * (M - 1) # imagine tracing stripes on grid
        
    print(total) # print out result
