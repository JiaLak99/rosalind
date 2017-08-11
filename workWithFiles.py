finput = open('rosalind_ini5.txt', 'r')
foutput = open('output.txt', 'w')
linenum = 0
text = finput.read()
split = text.splitlines()

for i in split:
    if linenum % 2 == 1:
        foutput.write(str(i) + '\n')
    linenum += 1

foutput.close()
finput.close()
