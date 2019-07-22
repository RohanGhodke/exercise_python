s1 = 'python 3.2'

letters = 0
digits = 0

for i in s1:
    if(i.isdigit()):
        digits += 1
    elif(i.isalpha() == True):
        letters += 1

print('Letters:',letters)
print('Digits:',digits)

