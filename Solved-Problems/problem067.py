#real	0m0.040s
#user	0m0.022s
#sys	0m0.013s

# The map function splits each number in a line with a comma
levels = [map(int, s.split()) for s in open("p067_triangle.txt").readlines()]

# I can apply the same method from problem 18
for i in range(98,-1,-1):
    for x in range(i+1):
        levels[i][x] = max(levels[i][x]+levels[i+1][x],levels[i][x]+levels[i+1][x+1])

print(levels[0][0])
