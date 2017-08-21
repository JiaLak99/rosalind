finput = open('rosalind_revc.txt', 'r')
linenum = 0
dna = finput.read()
split = dna.splitlines()

reversedna = ''
for letter in dna:
    if letter == 'A':
        reversedna = 'T' + reversedna
    elif letter == 'C':
        reversedna = 'G' + reversedna
    elif letter == 'G':
        reversedna = 'C' + reversedna
    elif letter == 'T':
        reversedna = 'A' + reversedna
print reversedna

finput.close()
