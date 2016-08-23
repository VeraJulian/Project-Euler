#real	0m0.073s
#user	0m0.051s
#sys	0m0.014s

from utils import is_prime
from utils import is_Pandigital

import itertools

permutations = list(itertools.permutations(['1','2','3','4','5','6','7']))

print max(''.join(permutations[i]) for i in range(1,5040) if is_prime(int(''.join(permutations[i]))))
