#real	0m0.152s
#user	0m0.127s
#sys	0m0.013s

# Finds Pythagorean triplet for which a + b + c = 1000

for a in range(1,1000):
    for b in range(a, 1000-a):
        cSquared = (a**2) + (b**2)
        c = cSquared**0.5
        if(a+b+c == 1000):
            magic_product = a*b*c
            print(magic_product)
            
