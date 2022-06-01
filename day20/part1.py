with open('input.txt') as home0:
    house = int(home0.read())//10
print(house)
for ho in range(10000, house):
    if ho % 30000 == 0: print(ho)
    summa = 0
    pip = 1
    while pip*pip < ho:
        if ho % pip == 0:
            summa += pip
            summa += ho//pip
        pip +=1

    if pip*pip == house:
        summa += pip
    if summa >= house:
        print('Yea', ho)
        output = open('output1.txt', 'w')
        output.write(str(ho))

        output.close()
        home0.close()
        break