#real	0m0.036s
#user	0m0.018s
#sys	0m0.013s

from utils import is_Pandigital

print max(str(i)+str(i*2) for i in range(9200,10000) if is_Pandigital(str(i)+str(i*2)))
