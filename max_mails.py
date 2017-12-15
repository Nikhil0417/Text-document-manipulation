name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
max = 0
lemon = dict()
ems = list()
for line in handle:
    if line.startswith('From:'):
		email = line.split()
		ems.append(email[1])
#print(ems)
for i in ems:
	lemon[i] = lemon.get(i,0) + 1
#print(lemon)
for i in lemon:
	if lemon[i] > max:
		max = lemon[i]
		em = i
print(em, max)
