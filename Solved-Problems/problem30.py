#real	0m1.835s
#user	0m1.788s
#sys	0m0.026s

total = 0
for i in range(10,354294):
    total += i if i == sum(int(digit)**5 for digit in str(i)) else 0
print total
