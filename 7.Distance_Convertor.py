'''
    function named convert_distance() to convert distances between kilometers and meters. 
    Your function should take two parameters: distance (a floating-point number) and unit (a string that can either be "km" for kilometers or "mtr" for meters). 
    The function should return a tuple with the converted distance as a floating-point value 
    and the corresponding unit.

    Your function should raise an ValueError when a negative number is passed or 
    when a different unit is passed to the function.

'''

def convert_distance(distance, unit):
    if distance>=0:
        if unit=="mtr":
            distance/=1000
            return (distance, "km")
        elif unit=="km":
            distance*=1000
            return (distance, "mtr")
        else:
            raise ValueError
    else:
        raise ValueError
    

# Example function calls
print(convert_distance(1.5, "km"))  # Expected output: (1500.0, "mtr")
print(convert_distance(3000, "mtr"))  # Expected output: (3.0, "km")
print(convert_distance(0, "mtr"))  # Expected output: (0.0, "km")