# Code Chef Practice (Beginner) Problem
# Lucky Four - Find the occurences of 4 in a given integer

T = int(input()) # test cases input

for t in range(T): # iterate over each test case
    
    number = list(input()) # transform integer input into list
        
    cnt = 0 # initialize counter
    for digit in number: # iterate over each digit of number
        if digit == '4': # verify if digit equals 4
            cnt += 1 # increase counter by 1

    print(cnt) # print counter result
