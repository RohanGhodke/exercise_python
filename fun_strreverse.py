s = input('Enter a string:')

def reverse(s):
    s1 = ''
    for i in s:
        s1 = i + s1
    return s1    

print("The reversed string is:",reverse(s))
