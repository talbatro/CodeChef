# Code Chef Practice (Beginner) Problem
# The Wave

def isOdd(num):
    return True if num&1 else False # use bitwise & (AND)

def biSearch(lst, num):

    start = 0 # initialize start
    end = len(lst) - 1 # intialize end

    while start <= end:
        pos = start + (end - start) // 2 # find middle position

        if num < lst[pos]:
            end = pos - 1
        elif num > lst[pos]:
            start = pos + 1
        else:
            return -1

    if num < lst[pos]:
        return pos
    elif num > lst[pos]:
        return pos + 1
    else:
        return -1

N, Q = map(int, input().split()) # input length of roots and querries

A = list(map(int, input().split())) # input roots
A.sort() # sort roots

for i in range(Q): # iterate over each querry
    number = int(input()) # input number of interest

    pos = biSearch(A, number) # use binary search to find position of number

    if pos == -1: # if we found a root
        print("0")
        continue # skip to next querry
    
    gre = N - pos # find how many roots are greater than number

    if isOdd(gre): # if it is odd, it's negative
        print("NEGATIVE")
    else: # if it is even, it's positive
        print("POSITIVE")
