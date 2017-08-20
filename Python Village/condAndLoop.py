a = 4023
b = 8602
if a % 2 == 0:
    a = a + 1
if b % 2 == 0:
    b = b - 1
sum = (a + b)/2 * ((b - a)/(2) + 1)
print sum
