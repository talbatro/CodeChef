# Code Chef Practice (Beginner) Problem
# Decrement OR Increment - If divisible by 4, increase by 1, else decrease by 1

N = int(input()) # get input

if N % 4 == 0: # check if number is divisible by 4
    print(N+1) # increase by 1
else:
    print(N-1) # decrease by 1
