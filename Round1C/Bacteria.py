import copy
def check(state, turn, R, C):

    count = {0:0, 1:0}
    found = False
    for r in range(R):
        for c in range(C):
            if state[r][c] == '.':
                
                changed = [r]
                state[r][c] = '0'
                rI = r + 1
                madeIt = True
                while rI < R:
                    if state[rI][c] == '0':
                        break
                    if state[rI][c] == '#':
                        madeIt = False
                        break
                    state[rI][c] = '0'
                    changed.append(rI)
                    rI += 1

                rI = r - 1
                while rI >= 0:
                    if state[rI][c] == '0':
                        break
                    if state[rI][c] == '#':
                        madeIt = False
                        break
                    state[rI][c] = '0'
                    changed.append(rI)
                    rI -= 1
                if madeIt:
                    output = check(state, (turn + 1) % 2, R, C)
                    if output[turn]:
                        count[turn] += 1
                    else: count[(turn + 1) % 2] += 1
                    found = True

                for i in changed:
                    state[i][c] = '.'



                changed = [c]
                state[r][c] = '0'
                cI = c + 1
                madeIt = True
                while cI < C:
                    if state[r][cI] == '0':
                        break
                    if state[r][cI] == '#':
                        madeIt = False
                        break
                    state[r][cI] = '0'
                    changed.append(cI)
                    cI += 1
                    
                cI = c - 1
                while cI >= 0:
                    if state[r][cI] == '0':
                        break
                    if state[r][cI] == '#':
                        madeIt = False
                        break
                    state[r][cI] = '0'
                    changed.append(cI)
                    cI -= 1
                if madeIt:
                    output = check(state, (turn + 1) % 2, R, C)
                    if output[turn]:
                        count[turn] += 1
                    else: count[(turn + 1) % 2] += 1
                    found = True
                for i in changed:
                    state[r][i] = '.'

    if not found:
        count[(turn + 1) % 2] = 1
    return count




T = int(input())
for test in range(1,T + 1): 
    R, C = list(map(int, input().split()))
    state = []
    for row in range(R):
        state.append(list(input()))
    
    output = check(state, 0, R, C)

    print("Case #{}: {}".format(test,output[0]))