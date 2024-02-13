'''             function is_prime_number in Python that checks if a given number is a prime number.
                The function should return True if the number is prime, and False otherwise.

                Input: A single number (can be positive, negative, or a floating point number).
                Output: True if the number is a prime number, False otherwise.
'''


def is_prime_number(n):
    n=int(n)
    if n>1:
        for i in range (2, n):
            if (n%i)==0:
                return False
                break
        else:
            return True

    else:
        return False
    

# Sample Function Calls for testing - Hit the run button to see the output
print(f"is_prime_number(3): {is_prime_number(3)}")  # Expected: True
print(f"is_prime_number(41): {is_prime_number(41)}")  # Expected: True
print(f"is_prime_number(6): {is_prime_number(6)}")  # Expected: False
print(f"is_prime_number(1): {is_prime_number(1)}")  # Expected: False
print(f"is_prime_number(-3): {is_prime_number(-3)}")  # Expected: False
print(f"is_prime_number(1.1): {is_prime_number(1.1)}")  # Expected: False
