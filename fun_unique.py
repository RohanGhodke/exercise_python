n = int(input('Enter the number of elements in the list:'))
i = 0
l = []
print('Enter the elements:')
while i < n:
    a = int(input())
    l.append(a)
    i += 1
print('The list is:')    

def unique(m):
    l1 = []
    for i in m:
        if i in l1:
            continue
        else:
            l1.append(i)
    print('The unique list is:',l1)  

unique(l)           