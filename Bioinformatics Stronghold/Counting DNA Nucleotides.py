finput = open('rosalind_dna.txt', 'r')
linenum = 0
string = finput.read()
split = string.splitlines()

print string   
print string.count('A')
print string.count('C')
print string.count('G')
print string.count('T')

finput.close()
