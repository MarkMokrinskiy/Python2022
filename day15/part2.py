from itertools import dropwhile, combinations

with open('input.txt', 'r') as INPUT:
    ingredient_names = []
    new_array = []
    for line in INPUT:
        line = line.replace(':', ' ')
        line = line.replace(',',' ')
        array = line.split()
        ingredient_names.append(array[0])
        array_1 = array.copy()
        for element in array:
            if element.isalpha() == True:
                array_1.remove(element)
        for i in range(len(array_1)):
            array_1[i] = int(array_1[i])
        new_array.append(array_1)
        array_1 = []
array = new_array


calories = []
for i in range(len(array)):
    calories.append(array[i][-1])


comb_array = []
for i in range(101):
    for j in range(101):
        for k in range(101):
            h = 100 - i - j - k
            if h >= 0:
                comb_array.append([h,i,j,k])

new_array = []
for i in range(len(array)):
    for j in range(len(array)):
        array_1.append(array[j][i])
    new_array.append(array_1)
    array_1 = []
array = new_array
new_array = []
for i in range(len(array)):
    new_array.append(array[i])

array = new_array
new_array = []

some_list = []
produce = 1
check_array = []
ch_array = []
for element in comb_array:
    for ar in array:
        SUM = 0
        for i in range(len(element)):
            SUM += ar[i]*element[i]
        if  SUM < 0:
            SUM = 0

        SUM2 = 0
        for i in range(len(element)):
            SUM2 += calories[i]*element[i]
        if SUM2 != 500:
            SUM = 0

        check_array.append(SUM)
        produce *= SUM
    ch_array.append(check_array)
    check_array = []
    some_list.append(produce)
    produce = 1

with open('output2.txt', 'w') as OUTPUT:
    OUTPUT.write(str(max(some_list)))