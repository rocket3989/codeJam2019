import math

tests = int(input())
for test in range(1:tests+1):
    
    N , F , B = list(map(int, input().split())) 
    
    for i in range(0,2**10):
        print()