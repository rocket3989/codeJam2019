import math

for test in range(int(input())):
    
    N , B, F = [int(x) for x in input().split()] 
    results = []
    for bitPos in range(5):
        for i in range(0,N):
            print((i >> bitPos) & 1, end= '')
        print()
        results.append([int(x) for x in input()])
    
    last = -1
    block = 0
    found = 0

    for b0, b1, b2, b3, b4 in zip(results[0], results[1], results[2],                                    results[3], results[4]):
        val = b0 + (b1 << 1) + (b2 << 2) + (b3 << 3) + (b4 << 4);
        # print(val)

        if last > val :
            for i in range(last + 1, 32):
                print(32 * block + i, end =' ')
                found += 1
            last = -1
            block += 1

        last += 1
        while last != val:
            print(32 * block + last, end= ' ')
            found += 1
            last += 1
    last += 1
    while found < B:
        print(32 * block + last, end= ' ')
        last += 1
        found += 1
    print()
    if int(input()) == -1:
        break