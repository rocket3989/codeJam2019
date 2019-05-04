def check(state, turn, R, C):

    count = {0:0, 1:0}

    for r in range(R):
        for c in range(C):
            if state[r][c] == '.':

                newstate = state

                newstate[r][c] = '0'
                rI = r + 1
                madeIt = True
                while rI < R:
                    if state[rI][c] == '0':
                        break
                    if state[rI][c] == '#':
                        madeIt = False
                        break
                    newstate[rI][c] = '0'
                    rI += 1
                rI = r - 1

                while rI >= 0:
                    if state[rI][c] == '0':
                        break
                    if state[rI][c] == '#':
                        madeIt = False
                        break
                    newstate[rI][c] = '0'
                    rI -= 1
                if madeIt:
                    output = check(newstate, (turn + 1) % 2, R, C)
                    if output[turn]:
                        count[turn] += 1
                    else: count[(turn + 1) % 2] += 1


                newstate = state
                cI = c + 1
                madeIt = True
                while cI < C:
                    if state[r][cI] == '0':
                        break
                    if state[r][cI] == '#':
                        madeIt = False
                        break
                    newstate[r][cI] = '0'
                    cI += 1
                    
                cI = c - 1

                while cI >= 0:
                    if state[r][cI] == '0':
                        break
                    if state[r][cI] == '#':
                        madeIt = False
                        break
                    newstate[r][cI] = '0'
                    cI -= 1
                    
                if madeIt:
                    output = check(newstate, (turn + 1) % 2, R, C)
                    if output[turn]:
                        count[turn] += 1
                    else: count[(turn + 1) % 2] += 1
    return count




T = int(input())
for test in range(1,T + 1): 
    R, C = list(map(int, input().split()))
    state = []
    for row in range(R):
        state.append(list(input()))
    
    output = check(state, 0, R, C)

    print(f"Case #{test}: {output[0]}")