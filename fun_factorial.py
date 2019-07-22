n = int(input('Enter a number:'))


def factorial(x):
    m = x
    f = 1
    
    while x > 0:
        f = f*x
        x -= 1
        
    print('Factorial of',m,'is:',f)   

if n < 0:
    print('The factorial of negative number cannot be calculated!')
else:
    factorial(n) 
        

