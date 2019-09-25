T = int(input())
for test in range(1,T + 1): 
    
    A = int(input())

    T, F = list(map(int, input().split()))

    moves = []
    for i in range(A):
        moves.append(input())

    print("Case #{}: ".format(test),end="")