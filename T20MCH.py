# Code Chef Practice (Beginner) Problem
# Cut the Board

R,O,C = map(int, input().split()) # input numbers as integer

left = 20 - O # how many overs are left to play
potential = left * 6 * 6 # how many runs can be scored

if potential + C > R: # is it enough to beat team A
    print("YES")
else:
    print("NO")
