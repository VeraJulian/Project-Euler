#real	0m1.192s
#user	0m0.914s
#sys	0m0.232s

import itertools

permutations = list(itertools.permutations(['0','1','2','3','4','5','6','7','8','9']))

print ''.join(permutations[999999])
