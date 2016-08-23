#real	0m0.200s
#user	0m0.134s
#sys	0m0.013s

text_file = open("p022_names.txt", "r")

names = text_file.read()
names = names.split('","')
text_file.close()

names[0] = names[0][1:]
names[5162] = names[5162][0:6]
names = sorted(names)

letters = ['','A','B','C','D','E','F','G','H','I','J','K','L','M',
           'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def letter_count(n):
    count = 0
    num_letters = len(names[n])
    for i in range(num_letters):
        for j in range(27):
            if names[n][i] == letters[j]:
                count += j
    return count*(n+1)

length = len(names)
print(sum(letter_count(i) for i in range(length)))
