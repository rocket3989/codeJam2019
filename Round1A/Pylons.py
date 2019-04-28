tests = int(input())
for test in range(0,tests):
    R , C = list(map(int, input().split())) 

    n = min(R,C)
    m = max(R,C)

    outcome = [[],[],[False,False,False,False,False,True],[False,False,False,False,True,True],[False,False,False,False,True,True],[False,False,False,False,False,True]]

    if outcome[n][m]:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
