finput = open('rosalind_ini6.txt', 'r')
foutput = open('output.txt', 'w')
linenum = 0
text = finput.read()
split = text.splitlines()

arr = text.split(" ")
dict = {}
for word in arr:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1
for word in dict:
    print word + " " + str(dict[word])

foutput.close()
finput.close()
