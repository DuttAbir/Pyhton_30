"""
    Reverses a given string.

    :param s: The string to be reversed.
    :return: The reversed string.
"""

def reverse_string(s):
    #length = len(s)
    #return(length)
    #rev_str=s[::-1]

    rev_str=""
    for i in s:
        rev_str=i+rev_str
    

    return rev_str


# Sample Tests
print("hello =>", reverse_string("hello"))  # Expected Output: olleh
print("codedamn =>", reverse_string("codedamn"))  # Expected Output: nmadedoc
print("racecar =>", reverse_string("racecar"))  # Expected Output: racecar
print("12345 =>", reverse_string("12345"))  # Expected Output: 54321
