
f = open("input.txt")
strings = f.readlines()
cnt_good_str = 0
List = []
List2 = []
List3 = []
vrper = None
vrper2 = None
vrper3 = None


def function1(Input):
	Input2 = ""
	for i in range(len(Input)-3):
		vr = str(Input[i]) + str(Input[i+1])
		Input2 = Input[i+2:]
		if vr in Input2:
			return(Input)
			break

def function2(Input):
	for i in range(len(Input)-2):
		if ord(Input[i]) == ord(Input[i+2]):
			return(Input)
			break



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

f.close()

with open("output2.txt", "w") as f:
	f.write(str(len(List2)))
