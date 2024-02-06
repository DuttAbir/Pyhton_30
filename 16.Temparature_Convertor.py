'''
        Name: convert_temperature
        Parameters:
            value (float): The temperature value to convert.
            input_unit (string): The unit of the input value ('c' for Celsius, 'f' for Fahrenheit, 'k' for Kelvin).
            output_unit (string): The unit to convert to ('c', 'f', 'k').

            If the input_unit and output_unit are the same, return the value rounded to two decimal places.
            If the input_unit or output_unit is not one of the specified values ('c', 'f', 'k'), the function's behavior is undefined.

'''


def convert_temperature(value, input_unit, output_unit):
    if input_unit=="c":
        if output_unit=="f":
            value=(9/5)*value+32
            return round(value,2)
        elif output_unit=="k":
            value+=273.15
            return round(value, 2)
    elif input_unit=="f":
        if output_unit=="c":
            value=(value-32)*(5/9)
            return round(value,2)
        elif output_unit=="k":
            value=(value+459.67)*(5/9)
            return round(value,2)
    elif input_unit=="k":
        if output_unit=="c":
            value-=273.15
            return round(value,2)
        elif output_unit=="f":
            value=value*(9/5)-459.67
            return round(value,2)
    else:
        raise TypeError
            


# Example function calls
print(convert_temperature(25, 'c', 'f'))  # Celsius to Fahrenheit
print(convert_temperature(10, 'c', 'k'))  # Celsius to Kelvin
print(convert_temperature(300, 'k', 'c'))  # Kelvin to Celsius
print(convert_temperature(273, 'k', 'f'))  # Kelvin to Fahrenheit
print(convert_temperature(68, 'f', 'k'))  # Fahrenheit to Kelvin
print(convert_temperature(32, 'f', 'c'))  # Fahrenheit to Celsius
