'''
        The function should be named factorial.
        It must use recursion to calculate the factorial.
        The function should take a single integer argument and return the factorial of that number.

'''


def factorial(n):
        return 1 if (n==1 or n==0) else n*factorial(n-1)

# Sample Tests
print("Factorial of 5:", factorial(5))   # Expected: 120
print("Factorial of 10:", factorial(10))  # Expected: 3628800
print("Factorial of 8:", factorial(8))   # Expected: 40320
print("Factorial of 18:", factorial(18))  # Expected: 6402373705728000