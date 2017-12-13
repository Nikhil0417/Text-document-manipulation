fname = input("Enter file name: ")
fh = open(fname)
lax = list()
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    point = line.strip()
    lax.append(float(point[19:]))
    count += 1
    #print("Average spam confidence:", float(point[19:]))
    #print(line[point:point+6])
for i in lax:
    total += i
print("Average spam confidence:",total/count)
#print(point[19:])
print("Done")
