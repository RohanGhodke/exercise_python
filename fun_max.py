print('Enter 3 numbers:')
i = 0
l = []
while i < 3:
    a = int(input())
    l.append(a)
    i += 1

def max():
    largest = l[0]
    i = 0
    for i in l:
        if i > largest:
            largest = i
    
    print('The largest among the 3 numbers is:',largest)

max()

