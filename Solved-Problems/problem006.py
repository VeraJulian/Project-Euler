#real	0m0.038s
#user	0m0.015s
#sys	0m0.013s

# Finds the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum

sum_of_squares = 0
for i in range(101): sum_of_squares += (i*i)

square_of_sum = 0
for i in range(101): square_of_sum += i
square_of_sum *= square_of_sum

print(square_of_sum - sum_of_squares)
