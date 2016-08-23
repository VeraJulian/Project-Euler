def prob44():
    pents = set()
    i = 0
    while True:
        i += 1
        p = (3*i*i - i) / 2
        pents.add(p)
        for n in pents:
            if p-n in pents and p-2*n in pents: 
                return p-2*n

print prob44()
