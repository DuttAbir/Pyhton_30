"""
    Determines whether the specified year is a leap year.
    
    Args:
    year (int): The year to be checked.

    Returns:
    bool: True if the year is a leap year, False otherwise.
"""

def is_leap_year(year):

    if (year%4==0):
        return True
    else:
        return False
    

print("2000 is a leap year:", is_leap_year(2000))  # Expected output: True
print("1997 is a leap year:", is_leap_year(1997))  # Expected output: False
print("2024 is a leap year:", is_leap_year(2024))  # Expected output: True
