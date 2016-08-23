#real	0m15.629s
#user	0m14.970s
#sys	0m0.241s

# 19-digit square

def all_digits(n):
    x = 0
    for i in range(1,10):
        if str(n)[x] == str(i): x += 2
        else: return False
    return x == 18

for i in range(1300000000,1400000000,10):
    x = i*i
    if all_digits(x):
        print i
        break
