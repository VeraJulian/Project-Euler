#real	0m0.106s
#user	0m0.081s
#sys	0m0.017s

'''
so we are only dealing with numbers from 10/11 to 98/99
so numerators 10..11..12..13...98
denominators 11..12..13...99
'''

from decimal import *
from fractions import Fraction

numerator = 1
denominator = 1
fracs = []

for i in range(10,99):
    str_i = str(i)
    for j in range(i+1,100):
        str_j = str(j)
        '''
        if str_i[0] == str_j[0] and str_i[1] != "0" and str_j[1] != "0":
            if Decimal(i)/Decimal(j) == Decimal(int(str_i[1]))/Decimal(int(str_j[1])):
                numerator *= int(str_i[1])
                denominator *= int(str_j[1])
                fract = Fraction(numerator,denominator)
                fracs.append(fract)

        if str_i[0] == str_j[1] and str_i[1] != "0" and str_j[0] != "0":
            if Decimal(i)/Decimal(j) == Decimal(int(str_i[1]))/Decimal(int(str_j[0])):
                numerator *= int(str_i[1])
                denominator *= int(str_j[0])
                fract = Fraction(numerator,denominator)
                fracs.append(fract)
        '''     
        if str_i[1] == str_j[0] and str_i[0] != "0" and str_j[1] != "0":
            if Decimal(i)/Decimal(j) == Decimal(int(str_i[0]))/Decimal(int(str_j[1])):
                numerator *= int(str_i[0])
                denominator *= int(str_j[1])
                fract = Fraction(numerator,denominator)
                fracs.append(fract)

print fracs[len(fracs)-1]
