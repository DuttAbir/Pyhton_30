'''
        The function should be named convert_binary.
        :It must accept a binary string (e.g., 0b1010) as input.
        :The function should return the decimal equivalent of the binary string.

        Ensure that your function can handle various lengths of binary strings.
        Remember, the use of direct binary-to-decimal conversion functions provided by Python is not allowed.   
        You need to implement the conversion logic manually.
'''

def convert_binary(binary_string):
    str1=binary_string[2:]
    str1=str1[::-1]
    dec=0
    n=1
    for i in range (0, len(str1)):
        dec+=int(str1[i])*n
        n*=2
    return dec 


# Example function calls and output printing
print("Decimal of '0b101':", convert_binary('0b101'))        # Expected Output: 5
print("Decimal of '0b0':", convert_binary('0b0'))            # Expected Output: 0
print("Decimal of '0b11101010':", convert_binary('0b11101010'))  # Expected Output: 234
