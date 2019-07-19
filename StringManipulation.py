s1 = input("Enter a string:")

l = len(s1)


i = l

if s1[i-3] == 'i':
    if s1[i-2] == 'n':
        if s1[i-1] == 'g':
            print(s1+"ly")
        else:
            print(s1+'ing')    
    else:
        print(s1+'ing')      
else:
    print(s1+'ing')          
