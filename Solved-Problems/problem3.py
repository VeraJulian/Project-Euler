#real	0m0.034s
#user	0m0.015s
#sys	0m0.012s

# Finds largest prime factor of 600851475143

n = 600851475143
i = 2

while i*i < n:
    while n % i == 0:
        n = n/i
    i += 1

print(n)
