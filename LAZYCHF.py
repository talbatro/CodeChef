# Code Chef Practice (Beginner) Problem
# Lazy Chef - Find the amount of work lazy Chef does

T = int(input()) # test cases input

for t in range(T): # iterate over each test case

    x, m, d = map(int, input().split()) # map each input to ints

    lazy_work = x * m # total lazy work
    delay_work = x + d # maximum delayed work
    
    actual_work = min(lazy_work, delay_work) # actual work is the smallest between the two

    print(actual_work) # print out result
