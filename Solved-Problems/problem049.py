#real	0m0.045s
#user	0m0.022s
#sys	0m0.015s

from utils import is_prime
import itertools

# Use a set in case the same permutations are found and are primes: 6299 and 9629
primes = set()

# Will use this var to create digit permutations
num = ''

# Start at 1488 since we were already given 1487 example
for i in range(1488,3400):
    # All three numbers need to be primes
    if is_prime(i) and is_prime(i+3330) and is_prime(i+6660):
        # Use for permutations
        num = str(i)
        #Determine which numbers to permute
        (s,t,u,v) = (num[0],num[1],num[2],num[3])
        permutations = list(itertools.permutations([s,t,u,v]))
        # Find all prime permutations and add them to our set
        for j in range(len(permutations)):
            if str(i+3330) == ''.join(permutations[j]) and is_prime(i+3330):
                # Since we are dealing with a set we can go ahead and add i here
                primes.add(i)
                primes.add(i+3330)
            if str(i+6660) == ''.join(permutations[j]) and is_prime(i+6660):
                primes.add(i+6660)
                
# Concatenate numbers to get answer
concat = ""
for num in primes: concat += str(num)
print concat
