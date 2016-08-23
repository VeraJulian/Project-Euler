#real	0m0.995s
#user	0m0.957s
#sys	0m0.026s

from utils import is_prime

primes = []
primes.append(23)
a = ["2","4","6","8","0"]
for i in range(23,800000):
    strs = str(i)
    if not any(digit in strs for digit in a) and is_prime(i):
        primes.append(i)

def trunc(n):
    n = str(n)
    for i in range(1,len(n)):
        if not is_prime(int(n[i:])) or not is_prime(int(n[:i])):
            return False
    return True

trunc_primes = [x for x in primes if trunc(x)]
print sum(trunc_primes)
