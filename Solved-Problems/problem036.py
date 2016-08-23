#real	0m1.979s
#user	0m1.923s
#sys	0m0.035s

def isDB_pal(x):
    #this is binary representation
    binary_num = str(int(bin(x)[2:]))

    #this is just the string representation of num
    string_num = str(x)
    
    return(binary_num == binary_num[::-1] and string_num == string_num[::-1])

print(sum(i for i in range(1000000) if isDB_pal(i)))
