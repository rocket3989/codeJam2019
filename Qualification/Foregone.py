tests = int(input())
for test in range(0,tests):
    inString = input()
    A = ""
    B = ""

    foundFour = False

    for s in inString:
        if s == '4':
            A += '2'
            foundFour = True
            B += '2'
        else:
            A += s
            if foundFour:
                B += '0'

    print("Case #{}: {} {}".format(test + 1, A, B))