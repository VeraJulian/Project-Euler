#real	0m0.033s
#user	0m0.017s
#sys	0m0.011s

# add the numerator and denominator for next denominator
# add the previous denominator to the new denominator to get next numerator
'''
3/2
7/5
17/12
41/29
99/70
239/169
577/408
'''

n,d,limit,count = 3,2,999,0

while limit:
    
    next_d = n+d
    next_n = d+next_d
    
    n,d = next_n,next_d
    
    limit -= 1

    if len(str(next_n)) > len(str(next_d)): count += 1

print count
