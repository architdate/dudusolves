# The last 4 digits of the series 1^1 + 2^2 + ... + 25^25

i = 0
for x in range(1, 26):
    i += x ** x
    
print(str(i)[-4:])
