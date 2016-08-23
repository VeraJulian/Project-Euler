#real	0m0.058s
#user	0m0.041s
#sys	0m0.011s

def prob52():
    i = 125873
    while True:
        i += 1
        two_x,three_x,four_x,five_x,six_x = 2*i,3*i,4*i,5*i,6*i
        s2x,s3x,s4x,s5x,s6x = str(two_x),str(three_x),str(four_x),str(five_x),str(six_x)

        if s2x.strip(s3x) == s3x.strip(s4x) == s4x.strip(s5x) == s5x.strip(s6x):
            return i
        
print prob52()
