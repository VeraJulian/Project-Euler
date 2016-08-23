#real	0m0.037s
#user	0m0.014s
#sys	0m0.013s

#12=6*2, 14=7*2, 16=8*2
#18=9*2, 20=10*2

# Finds the smallest positive number that is evenly divisble by numbers 1-20

primes = [11,13,17,19]
total = 2520

for i in primes: total *= i

#Multiply by 2 for reasons above (12 = 6*2, etc)
print(total * 2)
