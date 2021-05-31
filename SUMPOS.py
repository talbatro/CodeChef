# Code Chef Practice (Beginner) Problem
# Pair Me - Find if int can be written as sum of other

T = int(input()) # input test cases

for t in range(T): # iterate over each test case

    n = list(map(int, input().split())) # input number

    N = len(n) # get size of list

    possible = False # initialize a boolean
    for i in range(N): # iterate over each number
        if n[i] == sum(n) - n[i]: # check if number can be written as sum of the others
            possible = True
            break

    if possible: # if possible, print "YES"
        print("YES")
    else: # otherwise, print "NO"
        print("NO")
