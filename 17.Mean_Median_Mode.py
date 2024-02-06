'''
        The function should return a dictionary with keys as 'mean', 'median', and 'mode', and their respective calculated values.
        Additionally, the function should print these values.
        Make sure to round the output generated to two decimal places. 

'''

import statistics as st

def central_tendency(data):
    mean=round(st.mean(data),2)
    median=st.median(data)
    mode=st.mode(data)

    return {"mean": mean, "median":median, "mode": mode}



# Example function calls
print("Example 1:", central_tendency([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]))
print("Example 2:", central_tendency([5, 7, 12, 15, 21, 23, 23, 30, 34, 36, 40, 45, 50, 55]))
print("Example 3:", central_tendency([1, 1, 2, 3, 4, 5, 8, 13]))