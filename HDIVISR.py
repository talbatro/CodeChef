# Code Chef Practice (Beginner) Problem
# Highest Divisor - Find highest divisor between 1 and 10

N = int(input()) # get input as int

for i in range(10): # iterate over divisors
    div = 10 - i # start from the end
    if N % div == 0: # if divisor found, print it and break
        print(div)
        break
