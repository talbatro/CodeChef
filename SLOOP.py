# Code Chef Practice (Beginner) Problem
# Coldplay - How many times the song can be played completely

T = int(input()) # test cases input

for t in range(T): # iterate over each test case

    drive_time, song_time = map(int, input().split()) # map each input to int

    songs = drive_time / song_time # find number of times the song can be played
    songs = int(songs) # remove the decimal by converting to int

    print(songs) # print out result
