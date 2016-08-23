#real	0m0.080s
#user	0m0.034s
#sys	0m0.021s

from utils import sieve
from utils import is_prime

# We use the fact that in the longest sum of consecutive primes below one-thousand that adds to a prime,
# 2,3,5 are not present in the total ! 

primes = sieve(10000)
total = 0

for i in range(4):
    total = 0
    total += primes[i]
    for j in range(i+1,len(primes)):
        total += primes[j]
        if is_prime(total) and total < 1000000 and total > 990000:
            print total
