
import random

primes = []
num = 1
while(len(primes) < 26):
    num += 1
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                    break
        else:
            primes.append(num)

print(1)

"""
print("1 {}".format(len(primes)-1))
for x,y in zip(primes[::],primes[1::]):
    print(x*y,end=" ")
print()



print("1 99")
for i in range(100):
    print(random.choice(primes)*random.choice(primes),end =" ")
print()

"""
print(primes)