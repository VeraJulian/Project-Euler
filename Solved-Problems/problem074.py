#real	0m3.853s
#user	0m3.815s
#sys	0m0.027s

f = [1,1,2,6,24,120,720,5040,40320,362880]

def FacSum(n):
    temp = n
    facsum = 0

    while temp > 0:
        facsum += f[temp % 10]
        temp /= 10

    return facsum

def contains_479(n):
    n = str(n)
    return "4" in n and "7" in n and "9" in n

def prob74():
    result = 0

    for i in range(1,1000000):
        n = i
        seq = []

        if not contains_479(n):
            continue
    
        while n not in seq:
            seq.append(n)
            n = FacSum(n)

        if len(seq) == 60:
            result += 1

    return result

print prob74()
