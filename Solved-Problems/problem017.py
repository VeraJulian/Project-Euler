#real	0m0.038s
#user	0m0.016s
#sys	0m0.012s

ones = ["","one","two","three","four","five","six","seven","eight","nine"]
teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens = ["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

ones_to_19 = ["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen",
              "nineteen"]

hundreds = ["","onehundred","twohundred","threehundred","fourhundred","fivehundred","sixhundred","sevenhundred","eighthundred","ninehundred","onethousand"]
len_and = 3

def calc_length(n):
    count = 0
    if n%100:
        if n < 20: count += len(ones_to_19[n])
        if n > 19 and n < 100: count += len(tens[n/10]) + len(ones[n%10])
        elif n > 100:
            if (n%100)/10 == 1: count += len(hundreds[n/100]) + len_and + len(ones_to_19[(n%100)])
            else: count += len(hundreds[(n/100)]) + len_and + len(tens[((n%100)/10)]) + len(ones[n%10])
    else:
        count += len(hundreds[n/100])

    return count

print(sum(calc_length(i) for i in range(1,1001)))
