T = int(input())
for test in range(1,T + 1): 
    playCount = 0
    for i in range(1,21):
        print(i,100)
        playCount += 1
    playIn = 10
    while playCount < 100:
        print(playIn, 100)
        playCount+= 1
        playIn+= 1
        if playIn > 20:
            playIn = 10
    