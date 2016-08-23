#real	0m0.033s
#user	0m0.014s
#sys	0m0.012s

x,count = 0,0

for i in range(1,10):
    for j in range(1,50):
       x = i ** j
       if len(str(x)) == j:
           count += 1
           
print count
