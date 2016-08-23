#want biggest number with least divisors, hence prime product

from utils import sieve

primes = sieve(20)

total = 1
for p in primes:
    if total < 1000000:
        total *= p

print total/p
