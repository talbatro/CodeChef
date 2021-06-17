# Code Chef Practice (Beginner) Problem
# Save Water, Save Life - Find if all household can have water

import math

T = int(input()) # test cases number input

for t in range(T): # iterate over each test case
    H, x, y, C = map(int, input().split()) # map each input to variable

    tot = (x + math.floor(y/2)) * H # water required for all households

    if tot <= C: # check if there is enough available water
        print("YES") # print out result
    else:
        print("NO") # print out result
