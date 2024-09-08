import random
for a in range(1,30):
    i = random.randint(3,20)
    s = str(i)+' '
    for j in range(1,i):
        for k in range(j,i):
            if i % (j+k) == 0 and j != k:
                s += (str(j) + str(k))
    print(s)