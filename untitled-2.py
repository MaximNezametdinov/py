alf= "0123456789abcdefg"
for x in alf:
    f = int(f'26{x}34',17) + int(f'3{x}597',17)
    if f % 13 == 0:
        print(f//13)
        break