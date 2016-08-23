#real	0m0.138s
#user	0m0.113s
#sys	0m0.015s

champs_const = ""
i = 0
while len(champs_const) < 1000001:
    champs_const += str(i)
    i+=1

total = 1
for i in range(7): total *= int(champs_const[10**i])  
    
print total
