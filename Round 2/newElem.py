T = int(input())
for test in range(1,T + 1):

    elms = [] 
    
    A = int(input())
    for i in range(A):
        elms.append(tuple(map(int, input().split())))
    elms.sort()

    for x, y in zip(elms, elms[1:]):
        if x[1] > y[1]:
            print("Case #{}: 2".format(test))
            break
    else:
        print("Case #{}: 1".format(test))