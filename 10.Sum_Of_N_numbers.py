'''
        he function should be named sum_of_n.
        :It should take one argument, n, which is a positive integer.
        :The function should return the sum of all integers from 1 to n.
'''

def sum_of_n(n):
    sum=0
    for i in range (0,n+1):
        sum+=i

    return sum

# Test cases
print(sum_of_n(10))  # Expected output: 55
print(sum_of_n(25))  # Expected output: 325
print(sum_of_n(0))   # Expected output: 0
print(sum_of_n(100)) # Expected output: 5050
