#real	0m0.146s
#user	0m0.118s
#sys	0m0.016s

from utils import is_prime
import math

def distinct_prime_factors():
    for composite in range(35,10000,2):
        if is_prime(composite):
            continue
        else:
            smallest_composite = 0
            for i in range(1,int(math.sqrt(composite)+1)):
                if is_prime(composite-2*(i**2)):
                    smallest_composite = composite
            if not smallest_composite:
                        return composite
                    
print distinct_prime_factors()
