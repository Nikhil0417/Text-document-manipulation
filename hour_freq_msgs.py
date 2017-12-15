name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
time = list()
tup = list()
freq = dict()
for line in handle:
	if line.startswith('From'):
		a = line.split() # a is a list
		if a[0] == 'From':
			hour = a[5]
			scam = hour.split(':')
			#print(scam[0])
			time.append(scam[0])
#print(time)
for i in time:
	freq[i] = freq.get(i,0) + 1
#print(freq)
x = sorted(freq.items())
for k,v in x:
	print(k,v)
#print(x)
#for k,v in freq.items():
#	tup.append((k,v))
#	tup = tup.sort()
#print(tup)
