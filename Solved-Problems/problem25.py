#real	0m0.085s
#user	0m0.049s
#sys	0m0.016s

def fib():
    sum_fib = 2
    a,b = 1,1
    while len(str(b)) < 1000:
        a,b = b,a+b
        sum_fib += 1

    return sum_fib

print fib()
