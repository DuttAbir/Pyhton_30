'''
        Input: A list of elements (can be of any type).
        Output: A new list with unique elements from the input list, maintaining the original order.

        Empty List: If the input list is empty, the function should return None.
        Type Validation: The function should only accept a list as input. If any other type of argument is passed, the function must raise a TypeError.

'''


def unique_elements(lst):
    if type(lst) is list:
        if len(lst)>0:
            set_lst = set(lst)
            uniq_lst=list(set_lst)
            uniq_lst.sort(key=lst.index)
            return uniq_lst
        else:
            return None
    else:
        raise TypeError

# Example function calls
if __name__ == "__main__":
    print(unique_elements([1, 2, 2, 3, 3, 3, 4]))  # Output: [1, 2, 3, 4]
    print(unique_elements(["apple", "banana", "apple", "orange", "banana"]))  # Output: ["apple", "banana", "orange"]
    print(unique_elements([]))  # Output: None
    print(unique_elements("not a list"))  # ! This will raise a TypeError