T, F = list(map(int, input().split()))
for test in range(1,T + 1): 
    
    result = []
    
    counts = {'A':[],'B':[],'C':[],'D':[],'E':[]}
    for i in range(1, 596, 5):
        print(i)
        res = input()
        counts[res].append(i)


    for key, value in counts.items():
        if len(value) == 23:
            result.append(key)
            values = value
            break
    
    counts = {'A':[],'B':[],'C':[],'D':[],'E':[]}

    for i in values:
        print(i + 1)
        res = input()
        counts[res].append(i)

    for key, value in counts.items():
        if len(value) == 5:
            result.append(key)
            values = value
            break

    counts = {'A':[],'B':[],'C':[],'D':[],'E':[]}

    for i in values:
        print(i + 2)
        res = input()
        counts[res].append(i)

    for key, value in counts.items():
        if len(value) == 1:
            result.append(key)
            values = value
            break

    print(values[0] + 4)
    result.append(input())

    print(values[0] + 3)
    result.append(input())

    for c in result:
        print(c,end="")
    print()

    res = input()
    if res == 'N':
        break