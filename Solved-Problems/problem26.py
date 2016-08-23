#real	0m0.836s
#user	0m0.808s
#sys	0m0.018s

import decimal
from decimal import *

decimal.getcontext().prec = 2000 

def cycle_len(d):
    s = Decimal(1)/Decimal(d)
    for length in range(1,1000):
        if str(s)[30:30+length] == str(s)[30+length+1:30+2*length+1]:
            return length
    return None

longest = 0
digit = 0
for i in range(2,1000):
    if cycle_len(i) > longest:
        longest = cycle_len(i)
        digit = i

print digit
