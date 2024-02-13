"""
    This function takes an integer n, sums its digits, and continues summing the digits
    of the result until a single-digit number is obtained. This single-digit result is then returned.

"""

def sum_of_digits(n):
    while n>=10:
        sum=0
        while n>0:
            sum+=n%10
            n=n//10
        n=sum
    return n


# Example function calls and printing their outputs
if __name__ == "__main__":
    examples = [29, 12345, 45, 7, 987654, 0]
    for example in examples:
        print(f"sum_of_digits({example}) = {sum_of_digits(example)}")