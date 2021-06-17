# Code Chef Practice (Beginner) Problem
# Summer Heat - How many coconuts to stay alive

import math

T = int(input()) # input case number

for t in range(T): # iterate over each test case
    xa,xb,Xa,Xb = map(int, input().split()) # map inputs to variables

    A = math.ceil(Xa/xa) # number of type A coconuts needed
    B = math.ceil(Xb/xb) # number of type B coconuts needed

    print(A+B) # print sum
