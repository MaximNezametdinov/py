alf= "012"
for x in range(1,10000):
    f = 243**5+3**7-2-x
    k = 0
    while f > 0:
        if f % 3 == 2:
            k += 1
        f = f // 3
    if k == 20:
        print(x)
        break