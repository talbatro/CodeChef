# Code Chef Practice (Beginner) Problem
# Sum OR Difference - Find sum or difference if 1st number is greater

N1 = int(input()) # input 1st number
N2 = int(input()) # input 2nd number

if N1 > N2: # check if 1st is greater than 2nd
    print(N1 - N2) # print out difference
else:
    print(N1 + N2) # otherwise print out sum
