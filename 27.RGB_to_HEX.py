"""
        Converts RGB values to a hexadecimal color code.

        Parameters:
        red (int): Red component (0-255)
        green (int): Green component (0-255)
        blue (int): Blue component (0-255)

        Returns:
        str: Hexadecimal color code
"""


def dec_to_hex(n):
    hexVal = hex(n)
    hexVal=str(hexVal[2:4]).upper()
    if len(hexVal)<2:
        hexVal="0"+ hexVal

    return hexVal

def get_hexcode(red, green, blue):
    hexcode = "#"
    hexcode+= dec_to_hex(red)
    hexcode+= dec_to_hex(green)
    hexcode+= dec_to_hex(blue)

    return hexcode




# Example function calls
print(get_hexcode(255, 0, 0))   # Output: #FF0000
print(get_hexcode(0, 255, 255)) # Output: #00FFFF
print(get_hexcode(0, 0, 0))     # Output: #000000
print(get_hexcode(201, 0, 210)) # Output: #C900D2
print(get_hexcode(255, 255, 255)) # Output: #FFFFFF








