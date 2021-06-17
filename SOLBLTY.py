# Code Chef Practice (Beginner) Problem
# Solubility - How much sugar can be disolved

T = int(input()) # test cases

for t in range(T): # iterate over each test case
    X,A,B = map(int, input().split()) # map input to variables

    D = 100 - X # temperature increase possible

    S = A + D * B # sugar solutibility at 100 degrees

    amnt = 10 * S # 10 * 100ml in 1 Liter

    print(amnt) # print result
