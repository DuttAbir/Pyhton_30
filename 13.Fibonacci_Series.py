'''
        Your function should return a tuple of three numbers, adhering to the following rules:

        This function should take an integer N as input and return a tuple of three Fibonacci numbers: 
        :the (N-1)th, Nth, and (N+1)th in the sequence.
        :If N is 1 or greater, return the (N-1)th, Nth, and (N+1)th Fibonacci numbers.
        :If N is 0 or negative, return -1 for non-existent Fibonacci numbers.

        Negative Input: For any negative input, your function should return (-1, -1, -1), indicating non-existent Fibonacci indices.
        Zero Input: For an input of 0, the function should return (-1, -1, 0). Here, both -1 and 0 are considered as non-existent in the Fibonacci sequence context.

'''

def fibonacci_numbers(N):
    fibolist=[]
    n1=0
    n2=1
    nth=0
    if N>1:
        fibolist.insert(0,n1)
        fibolist.insert(1,n2)
        for i in range (1,N+1):
            nth=n1+n2
            fibolist.insert(i+1,nth)
            n1=n2
            n2=nth
    #return fibolist
        return (fibolist[N-1],fibolist[N],fibolist[N+1])
    elif N==1:
        return (-1,0,1)
    elif N==0:
        return (-1,-1,0)
    elif N<=1:
        return (-1,-1,-1)



# Example function calls
print(fibonacci_numbers(5))  # Expected: (3, 5, 8)
print(fibonacci_numbers(0))  # Expected: (-1, -1, 0)
print(fibonacci_numbers(-1)) # Expected: (-1, -1, -1)
print(fibonacci_numbers(4))  # Expected: (1, 2, 3)
print(fibonacci_numbers(1))  # Expected: (-1, 0, 1)
