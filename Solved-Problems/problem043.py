#real	0m10.241s
#user	0m9.972s
#sys	0m0.250s

from utils import is_Pandigital2
import itertools

permutations = list(itertools.permutations(['0','1','2','3','4','5','6','7','8','9']))

total = 0
for i in range(480000,2000000):
    num = ''.join(permutations[i])

    d2d3d4,d3d4d5,d4d5d6,d5d6d7 = int(num[1:4]),int(num[2:4]),int(num[3:6]),int(num[4:7])
    d6d7d8,d7d8d9,d8d9d10 = int(num[5:8]),int(num[6:9]),int(num[7:10])
    
    if is_Pandigital2(num) and (not d2d3d4%2) and (not d3d4d5%3) and (not d4d5d6%5) and (not d5d6d7%7) and (not d6d7d8%11) and (not d7d8d9%13) and (not d8d9d10%17):
        total += int(num)

print total
