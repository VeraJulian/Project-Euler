#real	1m4.287s
#user	1m3.208s
#sys	0m0.338s

_89_chain = set()
_1_chain = set()

#this just returns the next number in the chain of a number
def next_num(x):
    x,total = str(x),0
    for digit in x: total += int(digit)**2
    return total

# this method  make a list consisting of each number in a chain
def num_chain(n):
    chain = set()
    
    while True:
        n = next_num(n)
        chain.add(n)

        if n == 89 or n in _89_chain:
            for i in chain:
                _89_chain.add(i)
            return True

        if n == 1 or n in _1_chain:
            for i in chain:
                _1_chain.add(i)
            return False

    return False

tot = 0
for i in range(2,10000000):

    if i not in _89_chain:
        tot += num_chain(i)

    if i in _89_chain:
        tot += 1
    
    if i in _1_chain:
        continue
    
print "tot:",tot
