"""
    Checks if a list of three numbers can form a Pythagorean triplet.
    A Pythagorean triplet consists of three positive integers ( a ), ( b ), and ( c ), 
    such that ( a^2 + b^2 = c^2 ).
    
    Parameters:
    lst (list): A list of three numbers.
    
    Returns:
    bool: True if the numbers form a Pythagorean triplet, False otherwise.
    
    Raises:
    ValueError: If the input list does not contain exactly three numbers.

"""

def is_pythagorean_triplet(lst):

    if len(lst)==3:
        a=lst[0]
        b=lst[1]
        c=lst[2]
        if c**2==b**2+a**2:
            return True
        elif b**2==c**2+a**2:
            return True
        elif a**2==b**2+c**2:
            return True
        else:
            return False
    else:
        raise ValueError
    

# Example function calls and printing the output
if __name__ == "__main__":
        print(is_pythagorean_triplet([3, 4, 5]))      # Should return True
        print(is_pythagorean_triplet([10, 5, 24]))    # Should return False
        print(is_pythagorean_triplet([5, 3, 4]))      # Permutation of the first example, should return True
        print(is_pythagorean_triplet([1, 1, 1]))       # Not a Pythagorean triplet, should return False
        print(is_pythagorean_triplet([7, 24, 25]))    # A larger Pythagorean triplet, should return True
        print(is_pythagorean_triplet([9, 40, 41]))    # Another Pythagorean triplet, should return True

        print(is_pythagorean_triplet([1,2])) # Value Error 
