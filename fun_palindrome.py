s = input('Enter a string:')

def palindrome(s):
    s1 = ''
    for i in s:
        s1 = i + s1
    if s == s1:
        print('The string is palindrome')
    else:
        print('The string is not palindrome')

palindrome(s)             

