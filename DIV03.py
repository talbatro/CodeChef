# Code Chef Practice (Beginner) Problem
# Daanish and Problems - Find highest difficulty level

T = int(input()) # input test case number

for t in range(T): # iterate over each test case

    A = list(map(int, input().split())) # input list of number of problems
    K = int(input()) # input number of problems to remove

    level = 9 # initialize level
    while K > 0: # as long as problems can be removed

        K -= A[level] # find how many problems are left to be removed
        if K >= 0: # if there are still problems to remove
            A[level] = 0 # set current difficulty to 0 --> no more problems of this level

        level -= 1 # go to next lower difficulty

    for i in range(10): 
        if A[10-i-1] != 0: # check which difficulty still has problems
            level = 10 - i
            break
        
    print(level) # print out highest difficulty left
