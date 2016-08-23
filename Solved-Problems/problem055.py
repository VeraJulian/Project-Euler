#real	0m0.118s
#user	0m0.098s
#sys	0m0.013s

# max 49 iterations or the number is Lychrel
# we can assume 1-10 are not Lychrel?


def lychrel(x):
    for i in range(50):
        x += int(str(x)[::-1])
        if str(x) == str(x)[::-1]: return False
    return True

print sum(lychrel(i) for i in range(10,10000))
