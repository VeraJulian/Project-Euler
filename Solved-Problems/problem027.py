#real	0m1.119s
#user	0m1.089s
#sys	0m0.015s

# create a function that returns the number of primes quad function produces
# compare the previous with the next, and save

from utils import sieve
from utils import is_prime

# we know that b must be prime, negative or positive
b = sieve(1000)
neg_b = list(i for i in range(2,-1000,-1) if is_prime(i * -1))
new_b = neg_b + b

def num_primes(a,b):
    n = 0
    while is_prime( n**2 + a*n + b ):
        n += 1
    return n

max_a, max_b, num_n = 0,0,0

for a in range(-1000,1001):
    for b in new_b:
        n = num_primes(a,b)
        if n > num_n:
            max_a, max_b, num_n = a,b,n

print max_a * max_b
