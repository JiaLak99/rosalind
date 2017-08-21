finput = open('rosalind_rna.txt', 'r')
foutput = open('output.txt', 'w')
linenum = 0
dna = finput.read()
split = dna.splitlines()

rna = dna.replace('T', 'U')
foutput = rna.write()

foutput.close()
finput.close()
