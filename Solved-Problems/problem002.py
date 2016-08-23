#real	0m0.037s
#user	0m0.014s
#sys	0m0.012s

def sum_even_fib(n):
    sumfib = 0
    a,b = 1,1
    while b < n:
        a,b = b,a+b
        if b % 2 == 0:
            sumfib += b
    return sumfib

print(sum_even_fib(4000000))
