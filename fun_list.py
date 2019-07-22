n = int(input('Enter the number of elements in the list:'))
i = 0
l = []
while i < n:
    a = int(input())
    l.append(a)
    i += 1

def sum():
    s = 0
    i = 0
    while i < n:
        s = s + l[i]
        i += 1
    print('Sum of numbers in the list is:',s)

sum()    
