# Code Chef Practice (Beginner) Problem
# Valid Pair - Find if there is a pair of matching socks

socks = list(map(int, input().split(' '))) # input sock colors as ints

N = len(socks) # get number of socks

pair = False # initialize a boolean
for i in range(N): # iterate over each sock
    for j in range(i+1, N): # compare with other socks in list
        if socks[i] == socks[j]: # check if colors match
            pair = True 
            break # once found, break out of loop
    else:
        continue
    break

if pair:
    print("YES") # if pair found, print "YES"
else:
    print("NO") # otherwise, print "NO"
