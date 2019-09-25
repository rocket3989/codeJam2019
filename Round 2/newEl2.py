T = int(input())
for test in range(1,T + 1):

    elms = [] 
    
    A = int(input())
    for i in range(A):
        elms.append(tuple(map(int, input().split())))
   
    notSolved = True

    i, j = 1, 1
    madeTo = 0
    notBreakOut  = True
    while notBreakOut and notSolved:

        for inspect, (x, y) in enumerate(zip(elms, elms[1:])):
            
            diff =  (y[0] * i + y[1] * j) - (x[0] * i + x[1] * j) 
            if diff <= 0:
                if madeTo >= inspect:
                    notBreakOut = False
                
                if (y[0] * i + y[1] * (j + 1)) - (x[0] * i + x[1] * (j + 1)) >= diff:
                    #while (y[0] * i + y[1] * j) - (x[0] * i + x[1] * j)  <= 0:
                    last = j
                    j = -(-(i*(y[0] - x[0])) // (x[1] - y[1]))
                    if last == j:
                        j += 1
                else:
                    #while (y[0] * i + y[1] * j) - (x[0] * i + x[1] * j) <= 0:
                    last = i
                    i = -(-(j*(y[1] - x[1])) // (x[0] - y[0]))
                    if last == i:
                        i += 1
                madeTo = inspect
                break
        else:
            notSolved = False
    if not notSolved:
        print("Case #{}: {} {}".format(test,i,j))
    else:
        print("Case #{}: IMPOSSIBLE".format(test,i,j))