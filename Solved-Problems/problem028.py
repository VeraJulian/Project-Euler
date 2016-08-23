#real	0m0.031s
#user	0m0.014s
#sys	0m0.012s

'''
1,9,25: f(3)=9,f(5)=25
n^2

1,3,13,31: f(1)=1,f(3)=3,f(5)=13,f(7)=31
n^2 - 3n + 3

1,5,17,38: f(3)=5,f(5)=17,f(7)=37
n^2 - 2n + 2

1,7,21,43: f(3)=7,f(5)=21,f(7)=43
n^2 - n + 1

adding all together = 4n^2-6n+6
'''

total = 1
for i in range(3,1002,2): total += 4*(i**2)-(6*i)+6
print total
