f = open("input.txt")
strings = f.readlines()
cnt_good_str = 0
List = []
List2 = []
List3 = []
vrper = None
vrper2 = None
vrper3 = None

# Находим строки с гласными
def function1(somestr):
	cnt_vowels = 0
	for i in range(len(somestr)):
		if (somestr[i] == "a") or (somestr[i] == "e") or (somestr[i] == "i") or (somestr[i] == "o") or (somestr[i] == "u"):
			cnt_vowels += 1
	if cnt_vowels >= 3:
		return(somestr)

# Находим строки с двумя повторяющимися буквами
def function2(somestr):
	for i in range(len(somestr)-1):
		if somestr[i+1] == somestr[i]:
			return(somestr)
			break

# Находим строки с двумя неправильными буквами
def function3(somestr):
	wrongs = ""
	cnt = 0
	for i in range(len(somestr)-1):
		wrongs = str(somestr[i])+str(somestr[i+1])
		if (wrongs == "ab") or (wrongs == "cd") or (wrongs == "pq") or (wrongs == "xy"):
			cnt += 1
	if cnt == 0:
		return(somestr)

# Используем три цикла для фильтрации строк

for i in range(len(strings)):
	vrper = function1(str(strings[i]))
	if vrper != None:
		List.append(vrper)
	List = [line.rstrip() for line in List]

for j in range(len(List)):
	vrper2 = function2(str(List[j]))
	if vrper2 != None:
		List2.append(vrper2)
	List2 = [line.rstrip() for line in List2]

for l in range(len(List2)):
	vrper3 = function3(str(List2[l]))
	if vrper3 != None:
		List3.append(vrper3)
	List3 = [line.rstrip() for line in List3]

f.close()

with open("output1.txt", "w") as f:
	f.write(str(len(List3)))
