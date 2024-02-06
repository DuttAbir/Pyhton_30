'''
        Parameters: Two strings, str1 and str2.
        Output: The function should return a boolean value - True if str1 and str2 are anagrams, and False otherwise.
        Case Insensitivity: The function should treat uppercase and lowercase letters as the same.
        Non-Letter Characters: Non-letter characters (like spaces or punctuation) should not affect the outcome.
'''

def is_anagram(str1, str2):
    str1=str1.lower()
    str2=str2.lower()
    str3=""
    str3=str3.join(i for i in str1 if i.isalnum())
    str4=""
    str4=str4.join(i for i in str2 if i.isalnum())
    #return str3,str4
    lst1=list(str3)
    lst2=list(str4)
    lst1.sort()
    lst2.sort()
    #return lst1,lst2
    if lst1==lst2:
        return True
    else:
        return False
    

# Example function calls
print(is_anagram("Listen", "Silent"))  # Expected output: True
print(is_anagram("Hello", "World"))    # Expected output: False
print(is_anagram("Dormitory", "Dirty room"))  # Expected output: True