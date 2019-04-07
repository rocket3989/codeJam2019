
import math
import string

tests = int(input())
for test in range(0,tests):

    N , L = list(map(int, input().split())) 
    
    inputVals = list(map(int, input().split()))

    counter = 0

    for x,y in zip(inputVals[::],inputVals[1::]): #find if there are dupes at the start, & where they stop
        if (x != y):
            break
        counter += 1

    # 6 6 6 15
    #2 3 2 3  5

    # 6 6 15
    #3 2 3  5

    primes = [inputVals[counter] // math.gcd(inputVals[counter],inputVals[counter + 1])]
    
    for val in inputVals[counter:]:
        primes.append(val // primes[-1])
    
    for val in inputVals[counter:0:-1]:
        primes.insert(0,val // primes[0])

    
    """
    for x,y in zip(inputVals[::],inputVals[1::]):
        primes.append(math.gcd(x,y))

    primes.append(inputVals[-1]/primes[-1])

    """



    print (primes)
    
    keyPrimes = sorted(list(set(primes)))

    print(keyPrimes)

    primesAlpha = dict(zip(keyPrimes, string.ascii_uppercase))

    print(primesAlpha)

    print("Case #{}: ".format(test+1), end="") 

    for p in primes:
        print(primesAlpha[p], end = "")
    print()



    """



103 31
217 1891 4819 2291 2987 3811 1739 2491 4717 445 65 1079 8383 5353 901 187 649 1003 697 3239 7663 291 123 779 1007 3551 1943 2117 1679 989 3053

CJQUIZKNOWBEVYOFDPFLUXALGORITHMS

IPTHYJMNVBDUXNECOEKTWAKFNQHSGLR

10000 25
3292937 175597 18779 50429 375469 1651121 2102 3722 2376497 611683 489059 2328901 3150061 829981 421301 76409 38477 291931 730241 959821 1664197 3057407 4267589 4729181 5335543

SUBDERMATOGLYPHICFJKNQVWXZ
SUBDERMATOGLYPHICFJKNQVWXZ

2
103 31
217 1891 4819 2291 2987 3811 1739 2491 4717 445 65 1079 8383 5353 901 187 649 1003 697 3239 7663 291 123 779 1007 3551 1943 2117 1679 989 3053
10000 25
3292937 175597 18779 50429 375469 1651121 2102 3722 2376497 611683 489059 2328901 3150061 829981 421301 76409 38477 291931 730241 959821 1664197 3057407 4267589 4729181 5335543


"""