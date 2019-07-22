n = int(input("Enter a number:"))

if n == 1:
    print(n,'is not a prime number')
if n == 2:
    print(n,'is a prime number')

i = 2  

while i < n:
    if n % 1 == 0:
        print(n,'is not a prime number')
        break
    elif i == n-1:
        print(n,'is a prime number')
        break
