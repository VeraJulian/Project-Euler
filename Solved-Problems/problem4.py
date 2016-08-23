#real	0m0.616s
#user	0m0.596s
#sys	0m0.015s

# Finds the largest palindrome made from the product of two 3-digit numbers

palindromes = []
for i in range(100,1000):
    for j in range(100,1000):
        num = i * j
        if str(num) == str(num)[::-1]:
            palindromes.append(num)

print(max(palindromes))
