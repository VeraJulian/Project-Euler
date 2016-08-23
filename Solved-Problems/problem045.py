#real	0m0.174s
#user	0m0.137s
#sys	0m0.025s

Tris = set((n * (n + 1) / 2) for n in range(286, 100000))
Pentas = set((n * ((3 * n) - 1) / 2) for n in range(166, 100000))
Hexas = set((n * ((2 * n) - 1)) for n in range(144, 100000))
for i in Tris:
    if i in Pentas and i in Hexas:
        print i
