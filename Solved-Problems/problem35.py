#real	0m1.691s
#user	0m1.629s
#sys	0m0.045s

from utils import is_prime
from utils import sieve

# need a rotate function

# 197 --> 97(1) --> 7(1)(9)
def rotate(n):
    n = str(n)
    count = 1
    for i in range(1,len(n)):
        n = n[1:] + n[0]
        if is_prime(int(n)):
            count += 1
    return count == len(n)

primes = sieve(1000000)

total = 0

for prime in primes: total += rotate(prime)
print total
