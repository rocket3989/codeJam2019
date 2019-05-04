T = int(input())
for test in range(1,T + 1): 
    
    A = int(input())

    moves = []
    for i in range(A):
        moves.append(input())

    print("Case #{}: ".format(test),end="")

    count = 0

    output = []

    while True:
        taken = {'R':[],'P':[],'S':[]}

        for move in moves:
            taken[move[count % len(move)]].append(move)
            


        rock = (len(taken['R']) != 0) 
        paper = (len(taken['P']) != 0) 
        snip = (len(taken['S']) != 0)

        if rock:
            if paper:
                if snip:
                    print("IMPOSSIBLE",end="")
                    output = []
                    break
                else:
                    output.append('P')
                    moves = taken['P']
            else:
                if snip:
                    output.append('R')
                    moves = taken['R']
                else:
                    output.append('P')
                    break
        else:
            if paper:
                if snip:
                    output.append('S')
                    moves = taken['S']
                else:
                    output.append('S')
                    break
            else:
                if snip:
                    output.append('R')
                    break
                else: 
                    break
        count += 1

    for c in output:
        print(c,end="")
    print()
