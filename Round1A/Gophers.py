T, N, M = list(map(int, input().split()))
for test in range(0,T): 

    guesses = [17,16,13,11,9,7,5]
    mods = []
    
    for guess in guesses:
        
        print((str(guess)+ " ")*18)
        
        output = list(map(int, input().split()))

        count = 0
        for el in output:
            count += el

        count %= guess
        mods.append(count)

    for i in range(M):
        for mod, guess in zip(mods,guesses):
            if i % guess != mod:
                break
        else:
            print(i)
            break
    else:
        print(-1)

    res = int(input())
    if res == -1:
        break

