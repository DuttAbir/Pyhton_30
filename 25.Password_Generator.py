import random
import string

def generate_password(length=6, letters_count=2, numbers_count=2, symbols_count=2):

    lowerCaseLetters = string.ascii_lowercase
    UppercaseLetters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    password=[]

    if letters_count+numbers_count+symbols_count==length:
        password.extend(random.sample(lowerCaseLetters+UppercaseLetters, letters_count))
        password.extend(random.sample(digits, numbers_count))
        password.extend(random.sample(symbols, symbols_count))

        random.shuffle(password)

        return "".join(password)
    else:
        raise ValueError
    

# Test cases
print(generate_password(length=8, letters_count=3, numbers_count=3, symbols_count=2))
print(generate_password())
print(generate_password(length=10, letters_count=4, numbers_count=3, symbols_count=3))

