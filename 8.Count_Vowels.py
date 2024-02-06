'''
        function named count_vowels. This function takes a single string as input and returns a dictionary. 
        The dictionary should contain counts of each vowel ('a', 'e', 'i', 'o', 'u') found in the string. 
        It's important to note that the function should be case-insensitive 
        and include all vowels in the dictionary, even if their count is zero.

        The output should be a dictionary.
        :Each key is a vowel ('a', 'e', 'i', 'o', 'u').
        :The value for each key is the count of that vowel in the input string.
        :Include all vowels in the dictionary, even with a count of 0 if they are absent.
'''

def count_vowels(input_string):
   str2=""
   a_count=0
   e_count=0
   i_count=0
   o_count=0
   u_count=0
   str1=input_string.lower()
   str2=str2.join(i for i in str1 if i.isalnum())
   for i in str2:
      if i=="a":
         a_count+=1
      elif i=="e":
         e_count+=1
      elif i=="i":
         i_count+=1
      elif i=="o":
         o_count+=1
      elif i=="u":
         u_count+=1

   return{"a": a_count, "e":e_count, "i": i_count, "o": o_count, "u":u_count}


# Example function calls and printing their outputs
if __name__ == "__main__":
    example1 = print("Hello World =>",count_vowels("Hello World"))
    example2 = print("Python Programming =>",count_vowels("Python Programming"))
    example3 = print("Myths =>",count_vowels("Myths"))  # String with no vowels
