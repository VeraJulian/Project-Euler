#real	0m0.053s
#user	0m0.037s
#sys	0m0.011s

'''
a + b = c^2

a + b + c = p

a^2 + b^2 = (p-a-b)^2 = p^2 + a^2 + b^2 - 2pa - 2pb + 2ab

b = (p^2 - 2pa) / (2p - 2a)
'''

result,answer = 0,0

for p in range(2,1000,2):
    num_sol = 0
    for a in range(2, (p/3) ):
        if not(p*(p-2*a) % (2*(p-a))):
            num_sol += 1
        if num_sol > result:
            result = num_sol
            answer = p
            
print answer
