n = int(input('Enter the number of elements in the list:'))
i = 0
l = []
print('Enter the elements:')
while i < n:
    a = int(input())
    l.append(a)
    i += 1
print('The list is:')    

def even(m):
    l1 = []
    for i in m:
        if i % 2 == 0:
            l1.append(i)
    print('The even elements are:',l1)  

even(l)  