finput = open('rosalind_fib.txt', 'r')
linenum = 0
rep = finput.read()
split = rep.splitlines()
intsplit = [int(i) for i in split]

def rabbits(parent, child, months, reproduces):
    solution = 0
    if months == 1:
        solution = child
    else:
        solution = rabbits(child, parent * reproduces + child, months - 1, reproduces)
    return solution

print rabbits(0, 1, intsplit[0], intsplit[1])

finput.close()
