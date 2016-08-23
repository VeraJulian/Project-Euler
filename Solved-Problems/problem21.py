#real	0m3.907s
#user	0m3.872s
#sys	0m0.018s

from utils import factor_sum

def is_amic_pair(n):
    return n == factor_sum(factor_sum(n)) and n != factor_sum(n)

print sum(n if is_amic_pair(n) else 0 for n in range(1,10000))

