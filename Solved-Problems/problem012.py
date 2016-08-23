#real	0m1.390s
#user	0m1.351s
#sys	0m0.029s

from utils import divisors

# Finds first triangle number to have over five hundred divisors
for y in range(10000,1000000):
    x = (y*(y+1))/2
    if divisors(x) >= 500:
        print x
        break



