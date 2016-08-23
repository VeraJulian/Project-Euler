#real	0m0.429s
#user	0m0.406s
#sys	0m0.014s

from utils import fact_sum

print sum(i for i in range(3,50000) if fact_sum(i) == i)
