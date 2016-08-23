#real	0m0.173s
#user	0m0.148s
#sys	0m0.015s

# Finds the 10,001st prime number

from utils import is_prime

primes = [2,3,5,7,11,13]
count,i = (0,14)

while(len(primes) < 10001):
    if is_prime(i):
        primes.append(i)
        i = i+1
    else:
        i = i+1

print(primes[10000])
