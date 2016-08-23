#real	0m0.079s
#user	0m0.061s
#sys	0m0.012s

from utils import choose

values = 0
for n in range(5,101):
    for r in range(4,n):
        if choose(n,r) > 1000000:
            values += 1

print values
