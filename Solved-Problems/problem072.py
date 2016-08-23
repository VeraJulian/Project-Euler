#real	0m1.400s
#user	0m1.345s
#sys	0m0.044s

limit = 1000001
phi = range(1000001)
result = 0

for i in range(2,limit):
    if phi[i] == i:
        for j in range(i,limit,i):
            phi[j] = phi[j] / i * (i-1)
    result += phi[i]

print result
