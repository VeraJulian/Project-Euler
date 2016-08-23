#real	0m0.140s
#user	0m0.103s
#sys	0m0.015s

from utils import is_Pandigital

p = set()
for i in range(2,50):
    for j in range(1,2000):
        if is_Pandigital(str(i)+str(j)+str(i*j)):
            p.add(i*j)

print sum(p)
