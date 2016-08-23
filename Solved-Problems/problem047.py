#real	0m0.487s
#user	0m0.464s
#sys	0m0.014s

from utils import sieve

primes = sieve(700)

def four_prime_divisors(n):
    divisors = []
    for i in range(1,len(primes)-1):
        if n % primes[i] == 0: divisors.append(primes[i])
    return len(divisors)==4

for i in range(100000,135000):
    if four_prime_divisors(i) and four_prime_divisors(i+1) and four_prime_divisors(i+2) and four_prime_divisors(i+3):
        print i
