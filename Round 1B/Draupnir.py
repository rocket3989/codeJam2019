T, M = list(map(int, input().split()))
for test in range(0,T): 

    r = [0,0,0,0,0,0,0]
    inp = [0,0,0,0]
    for W in range(4, 4 + M):
        print(W)
        inp.append(int(input())) 

    r[1] = (inp[7] - inp[6]) // 64

    r[3] = (inp[9]-inp[8] - 256 * r[1]) // 4

    r[5] = inp[5] - inp[4] - 16 * r[1]

    r[2] = (inp[8] - 2*inp[4] - (256 - 32)*r[1]) // 8

    r[4] = (inp[8] - inp[7] - 8*r[2] - 128 * r[1]) // 2

    r[6] = (inp[6] - inp[5] - 4*r[2] - 2*r[3] - 32* r[1])

    for out in r[1::]:
        print(out, end=" ")
    print()