n = int(input('Enter the number of elements in the list:'))
i = 0
l = []
while i < n:
    a = int(input())
    l.append(a)
    i += 1

def sum():
    sum = 0
    for i in l:
        sum = sum + l[i]
    print('Sum of numbers in the list is:',sum)

sum()    
