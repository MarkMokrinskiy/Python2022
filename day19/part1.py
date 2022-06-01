import re
with open('input.txt') as home0:
    home = home0.read().split('\n')

def all_variants(template, start, end):
    indices = [m.start() for m in re.finditer(start, template)]
    ln = len(start)
    return [template[:i]+end+template[i+ln:] for i in indices]

template = home[-1]
rules = [line.split(" => ") for line in home[:-2]]
start = [rul[0] for rul in rules]
end = [rul[-1] for rul in rules]

molecules = set()

for i,l in zip(start,end):
    molecules.update(all_variants(template,i,l))

output = open('output1.txt', 'w')
output.write(str(len(molecules)))

output.close()
home0.close()