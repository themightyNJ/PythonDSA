'''
Creating a function that calls itself for repetitive statements, here, to find factorial.
Mathematically, Factorial function can be represented as Factorial(n) = n*Factorial(n-1)
'''

def Factorial(n):
    '''
    Creating a base case so that recursive function do not become infinite loop.
    Every recursive function should have atleast 1 base case.
    And every recursive function should eventually reach the base case at some point.
    '''
    if n == 0:
        return 1
    else:
        return n*Factorial(n-1)

'''Testing the function'''
number1 = 5
print("Factorial of ", number1," is : ",Factorial(number1))
number2 = 0
print("Factorial of ", number2," is : ",Factorial(number2))
