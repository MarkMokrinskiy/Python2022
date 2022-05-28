with open("input.txt") as f:
    text = ''.join(f.readlines())

def replace_all(text, srch, repl):            #Функция для замены букв на числа
  for i in range(0, len(srch)):
    text = text.replace(srch[i], repl[i])
  return text

lis = text.split(sep='+')              # Разделение слов
fw = lis[0]
sw = lis[1].split(sep='=')[0]
tw = lis[1].split(sep='=')[1]
letters = []
u = 0
for l in text:                             #Для того что бы выписать все встречающие буквы
    if l not in ('+', '='):
        if l not in letters:
            letters.append(l)

if len(letters) > 10:                        #Чисел у нас всего десять, это условие проверяет возможно ли решить ребус
    print('No solution')
    u = 100
tops, counters = [], []                       #Необходимые условия для решения функции, показанной  в начале
for i in range(0, len(letters)):
    tops.append(10 - i)
    counters.append(0)

canExit = False
while (not(canExit)) or u<1:                                #Цикл для подбора чисел

    numbers = ['0','1','2','3','4','5','6','7','8','9']     # Для того, что бы числа менялись
    substs = []
    for i in range(0, len(tops)):
        substs.append(numbers[counters[i]])
        del numbers[counters[i]]

    fwo = replace_all(fw, letters, substs)
    swo = replace_all(sw, letters, substs)
    two = replace_all(tw, letters, substs)

    try:                                             # Проверка условия. Подходит ли нам комбинация? Сразу проверка нуля в начале
        if int(fwo)+int(swo)==int(two) and int(list(fwo)[0])!= 0 and int(list(swo)[0])!= 0 and int(list(two)[0])!= 0:
            answer = (fwo + '+' + swo + '=' + two)
            u =+ 1

    except:
        None

    N = 0
    inc = 1
    while (N < len(counters) and inc > 0):
        counters[N] += inc
        inc = 0
        if (counters[N] == tops[N]):
            counters[N] = 0
            inc = 1
            N += 1

    canExit = True
    for i in range(0, len(tops)):
        canExit &= (counters[i] == tops[i] - 1)


if u == 0:                #Переменнная u нужна для того что бы в случае отсутсвия решение была возможность прописать No solution
    answer = 'No solution'

with open('output1.txt', 'w') as f:
    print(answer), file=f)