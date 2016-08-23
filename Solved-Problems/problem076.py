#real	0m0.039s
#user	0m0.020s
#sys	0m0.013s

target = 100
ns = range(1,target)

ways = [1]+[0]*target

for n in ns:
    for i in range(n,target+1):
        ways[i] += ways[i-n]

print ways[target]
