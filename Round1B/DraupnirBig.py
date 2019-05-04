T, M = list(map(int, input().split()))
for test in range(0,T): 

    r = [0,0,0,0,0,0,0]
    inp = []
    
    print(200)
    inp.append(int(input())) 

    print(56)
    inp.append(int(input()))

    r[6] = (inp[0] % 2 ** 40) // 2 ** 33

    inp[0] -= r[6] * 2 ** 33

    r[5] = (inp[0] % 2 ** 50) // 2 ** 40

    inp[0] -= r[5] * 2 ** 40

    r[4] = inp[0] // 2 ** 50

    inp[1] -= r[4] * 2 ** 14 + r[5] * 2 ** 11 + r[6] * 2 ** 9

    r[3] = (inp[1] % 2 ** 28) // 2 ** 18

    inp[1] -= r[6] * 2 ** 18

    r[2] = (inp[1] % 2 ** 56) // 2 ** 28

    inp[1] -= r[5] * 2 ** 28

    r[1] = inp[1] // 2 ** 56

    for out in r[1::]:
        print(out, end=" ")
    print()

    res = int(input())
    
    if res == -1:
        exit()