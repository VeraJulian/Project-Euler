#real	0m0.152s
#user	0m0.126s
#sys	0m0.015s

from utils import word_value

text_file = open("p042_words.txt", "r")
words = text_file.read()
words = words.split('","')
text_file.close()
words[0] = words[0][1:]
words[1785] = words[1785][0:5]

t_n = []
for n in range(1,21):
    t_n.append(int(.5*n*(n+1)))

t = 0
for i in words:
    for j in t_n:
        if word_value(i) == j:
            t += 1
print t
