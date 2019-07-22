n = int(input("Enter lower bound:"))
m = int(input("Enter upper bound:"))
x = int(input("Enter the number to check if it is in the range:"))

def rang():
    if (x >= n and x <= m):
        print(x,'is in range')
    else:
        print(x,'not in range')

rang()            