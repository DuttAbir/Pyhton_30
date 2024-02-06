def square_numbers(numbers):
    sqr_lst=[]
    for i in numbers:
        sqr_lst.append(round(i*i, 2))

    return sqr_lst



# Example function calls and printing the output
print(square_numbers([2, 3]))  # Should return [4, 9]
print(square_numbers([-2, 2.3]))  # Should return [4, 5.29]
print(square_numbers([]))  # Should return []