#real	0m0.926s
#user	0m0.896s
#sys	0m0.015s

from utils import factor_sum

total = 0
abundants = set()
 
for n in range(1, 28123):
    if factor_sum(n) > n: abundants.add(n)
    if not any( (n-a in abundants) for a in abundants ):
        total += n
        
print total
