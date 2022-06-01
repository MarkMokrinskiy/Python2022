with open('input.txt') as home0:
    home = home0.read().split('\n')

template = home[-1]

changeling = [(l.split()[0], l.split()[-1]) for l in home if ' => ' in l]

kl = dict()

for i in changeling:
    ap = 0
    for j in i[-1]:
        if j.isupper():
            ap +=1
    kl[i] = ap

changeling = list(kl.items())
changeling.sort(key=lambda x: x[-1])
changeling = [i[0] for i in changeling]

lst = changeling[::-1]

steps = 0

while template != 'e':
    for l, r in lst:
        if r in template:
            template = template.replace(r, l, 1)
            steps += 1
            break

print(steps)
output = open('output2.txt', 'w')
output.write(str(steps))

output.close()
home0.close()