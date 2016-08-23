#real	0m0.844s
#user	0m0.820s
#sys	0m0.015s

#1,3,13... = n^2 - 3n + 3
#1,7,21... = n^2 - n + 1
#1,5,17.. = n^2 - 2n + 2

from utils import is_prime

num_primes, n, avg = 0, 1, 1

while avg >= 0.10:
    n += 2
    num_primes += is_prime(n**2 - 3*n + 3) + is_prime(n**2 - n + 1) + is_prime(n**2 - 2*n + 2)
    avg = num_primes / (2.0 * n)    # the decimal forces a float calculation

print n
