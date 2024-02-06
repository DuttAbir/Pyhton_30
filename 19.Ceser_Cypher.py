"""
    A generalized function to either encrypt or decrypt a text using Caesar cipher.
    :param text: The input string to be encrypted or decrypted.
    :param shift: The shift value for the cipher.
    :param encrypt: Boolean to determine the operation mode (True for encrypt, False for decrypt).
    :return: The encrypted or decrypted string.
"""
letters = "abcdefghijklmnopqrstuvwxyz"

def caesar_cipher(text, shift, encrypt=True):
    if encrypt:
        cypherText=""
        for j in text:
            if j.isalpha():
                j=j.lower()
                index=letters.find(j)
                if index==-1:
                    cypherText+=j
                else:
                    new_index = index + shift
                    if new_index>= 26:
                        new_index-=26
                    cypherText+=letters[new_index]
            else:
                cypherText+=j

        return cypherText
    
    else:
        DecypherText=""
        for j in text:
            if j.isalpha():
                j=j.lower()
                index=letters.find(j)
                if index==-1:
                    DecypherText+=j
                else:
                    new_index = index - shift
                    if new_index<0:
                        new_index+=26
                    DecypherText+=letters[new_index]
            else:
                DecypherText+=j
                    
        return DecypherText



def encrypt(text, shift):
    return caesar_cipher(text, shift, encrypt=True)

def decrypt(text, shift):
    return caesar_cipher(text, shift, encrypt=False)



# Examples and test cases
if __name__ == "__main__":
    # Challenge 1
    encrypted_text_1 = encrypt("hello world", 5)
    decrypted_text_1 = decrypt(encrypted_text_1, 5)
    print(f"Encrypted: {encrypted_text_1}, Decrypted: {decrypted_text_1}")

    # Challenge 2
    encrypted_text_2 = encrypt("codedamn", 8)
    decrypted_text_2 = decrypt(encrypted_text_2, 8)
    print(f"Encrypted: {encrypted_text_2}, Decrypted: {decrypted_text_2}")

    # Challenge 3
    encrypted_text_3 = encrypt("Python 3.8!", 12)
    decrypted_text_3 = decrypt(encrypted_text_3, 12)
    print(f"Encrypted: {encrypted_text_3}, Decrypted: {decrypted_text_3}")

    # Challenge 4
    encrypted_text_4 = encrypt("Welcome to codedamn 2023!", 23)
    decrypted_text_4 = decrypt(encrypted_text_4, 23)
    print(f"Encrypted: {encrypted_text_4}, Decrypted: {decrypted_text_4}")
