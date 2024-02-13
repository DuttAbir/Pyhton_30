"""
    Generate a list of even numbers from 1 to n (inclusive) using list comprehension.

    Parameters:
    n (int): The upper limit of the range

    Returns:
    list: A list of even numbers within the specified range
"""
def list_even_numbers(n):
    lst=[]
    for i in range (1, n+1):
        lst.append(i)
    evens = []
    evens = [i for i in lst if i%2==0]
    return evens


# Example function calls
print("Output for n=5:", list_even_numbers(5))
print("Output for n=30:", list_even_numbers(30))
print("Output for n=15:", list_even_numbers(14))