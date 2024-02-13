'''         create a function named is_palindrome to determine whether a given string is a palindrome.
            A palindrome is a word or phrase that reads the same forwards and backwards.
            It should take a string as input and return:
                True if the string is a palindrome.
                False if the string is not a palindrome.
                None in the case of an empty string
'''

def is_palindrome(s):
    st=s.lower()
    str1=""
    str1=str1.join(i for i in st if i.isalnum())
    str2 = str1[::-1]
    if (str2==str1):
        if len(s)==0:
            return None
        else:
            return True
    else:
        return False
    

# Example function calls
print(is_palindrome("racecar"))  # Should return True
print(is_palindrome("codedamn"))  # Should return False
print(is_palindrome(""))         # Should return None
print(is_palindrome("A man, a plan, a canal: Panama"))  # Should return True
print(is_palindrome("No lemon, no melon"))              # Should return True

