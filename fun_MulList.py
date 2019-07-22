n = int(input('Enter the number of elements in the list:'))
i = 0
l = []
print('Enter the elements:')
while i < n:
    a = int(input())
    l.append(a)
    i += 1

def multiply():
    m = 1
    i = 0
    while i < n:
        m = m * l[i]
        i += 1
    print('Multiplication of numbers in the list is:',m)

multiply()    