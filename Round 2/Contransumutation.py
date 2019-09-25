T = int(input())
for test in range(1,T + 1):

    recipes = [] 
    
    A = int(input())
    for i in range(A):
        recipes.append(tuple(map(int, input().split())))
    
    counts = list(map(int, input().split()))

    maxLead = counts[0]

    newCounts = counts.copy()

    initCounts = counts.copy()

    diffCount = [0]*A

    runCount = 0


    #run once without spending lead


    while True:
        runCount += 1
        #for count, recipe in zip(newCounts if runCount % 1 else reversed(newCounts), recipes if runCount % 1 else reversed(recipes)):
        
        for i, (count, recipe) in enumerate(zip(newCounts, recipes)):
            if count and i != 0:
                newCounts[i] -= 1
                newCounts[recipe[0] - 1] += 1
                newCounts[recipe[1] - 1] += 1
        
        for i, (x, y) in enumerate(zip(counts, newCounts)):
            diffCount[i] = y - x
        
        if diffCount[0] == -1:
            maxLead = max(maxLead, counts[0])
        
        minOf = 0
        minCount = 0

        for x, y in zip(diffCount[1::], newCounts[1::]):
            if x * y < minOf:
                minCount = y

        if minCount:
            for x, y in zip(diffCount, newCounts):
                y += x*y*minCount

        elif runCount > A + 1:
            if diffCount[0] > 0:
                print("Case #{}: UNBOUNDED".format(test))
                bound = False
                break
            else:
                maxLead = max(maxLead, newCounts[0])
                bound = True
                break
        
        counts = newCounts.copy()



    newCounts = initCounts.copy()

    counts = initCounts.copy()

    diffCount = [0]*A

    runCount = 0



    while bound:
        runCount += 1
        #for count, recipe in zip(newCounts if runCount % 1 else reversed(newCounts), recipes if runCount % 1 else reversed(recipes)):
        
        for i, (count, recipe) in enumerate(zip(newCounts, recipes)):
            if count and (runCount < A + 1 or i != 0):
                newCounts[i] -= 1
                newCounts[recipe[0] - 1] += 1
                newCounts[recipe[1] - 1] += 1
        
        for i, (x, y) in enumerate(zip(counts, newCounts)):
            diffCount[i] = y - x
        
        if diffCount[0] == -1:
            maxLead = max(maxLead, counts[0])
        
        minOf = 0
        minCount = 0

        for x, y in zip(diffCount[1::], newCounts[1::]):
            if x * y < minOf:
                minCount = y

        if minCount:
            for x, y in zip(diffCount, newCounts):
                y += x*y*minCount

        elif runCount > A + 1:
            if diffCount[0] > 0:
                print("Case #{}: UNBOUNDED".format(test))
                break
            else:
                print("Case #{}: {}".format(test, maxLead))
                break
        
        counts = newCounts.copy()