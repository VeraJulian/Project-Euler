# Numbers raised to 90-100 have the most digits so we start with 90^90

prev,answer,num = 0,0,0

for base in range(90,101):
    for power in range(90,101):
        x = str(base ** power)
        num = sum(int(digit) for digit in x)

        if num > prev:
            prev = num
            answer = prev

print answer
