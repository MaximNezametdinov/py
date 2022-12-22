alf= "0123456789abc"
for x in alf:
    f = int(f'186{x}4',13) + int(f'5{x}716',13)
    if f % 11 == 0:
        print(f//11)
        break