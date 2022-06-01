with open('input.txt') as home0:
    house = int(home0.read())//11

for ho in range(100, house):
    if ho % 10000 == 0: print(ho)

    summa = 0
    pip = 1

    while pip <= 50:
        if ho % pip == 0:
            summa += ho//pip
        pip +=1

    if summa >= house:
        print('Yea', ho)

        output = open('output2.txt', 'w')
        output.write(str(ho))

        output.close()
        home0.close()
        break