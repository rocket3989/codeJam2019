

elms = [] 

for i in range(1,4):
    for j in range(1,4):
        elms.append(tuple((i,j)))

i, j = 1, 1

for elm in elms:
    print(i*elm[0] + j*elm[1], end = ' ')
print()
i, j = 3, 2 

for elm in elms:
    print(i*elm[0] + j*elm[1], end = ' ')
print()
i, j = 4, 1

for elm in elms:
    print(i*elm[0] + j*elm[1], end = ' ')
print()