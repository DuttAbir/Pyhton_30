def is_power_of_two(number):
    
    if number<= 0:
        return False
    
    elif number==1:
        return True
    
    else: 
        if number%2!=0:
            return False
        else:   
            for i in range (0, number):
                if pow(2, i)==number:
                    return True
            return False




# Test cases as examples
print("is_power_of_two(4):", is_power_of_two(4))  # Should return True
print("is_power_of_two(6):", is_power_of_two(6))  # Should return False
print("is_power_of_two(8):", is_power_of_two(8))  # Should return True
print("is_power_of_two(7):", is_power_of_two(7))  # Should return False
print("is_power_of_two(1):", is_power_of_two(1))  # Should return True (2^0)
print("is_power_of_two(0):", is_power_of_two(0))  # Should return False (Edge case)
