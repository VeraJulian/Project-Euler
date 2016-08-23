#real	0m2.285s
#user	0m2.166s
#sys	0m0.074s

num_steps = {}

def collatz_steps(n):
    steps = 1
    while(n - 1):
        if n in num_steps:
            return steps + num_steps[n]
        else:
            if n % 2 == 0:
                n = n/2
            else:
                n = (3*n)+1
        steps+=1
    return steps

def max_collatz():
    (max_steps,n) = (0,0)
    for i in range(1,1000000):
        steps = collatz_steps(i)
        num_steps[i] = steps
        if steps > max_steps:
            max_steps = steps
            n = i
    return n

print(max_collatz())
