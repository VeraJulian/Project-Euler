#real	0m0.053s
#user	0m0.033s
#sys	0m0.013s

powers = []

for a in range(2,101):
    for b in range(2,101):
        powers.append(a**b)

print len(set(powers))
