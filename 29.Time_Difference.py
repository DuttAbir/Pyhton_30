from datetime import datetime


def time_difference(start, end):

    timeNow= datetime.strptime(start, "%H:%M")
    timeThen=datetime.strptime(end, "%H:%M")

    dif = timeThen-timeNow

    dif_in_sec= dif.total_seconds()

    min= dif_in_sec//60

    hour= min//60

    if hour<0:
        hour+=24

    min= min%60

    


    return({'hours': int(hour), 'minutes': int(min)})


# Example function calls and print statements
print(time_difference('02:25', '3:00'))  # Expected Output: {'hours': 0, 'minutes': 35}
print(time_difference('23:15', '00:30')) # Expected Output: {'hours': 1, 'minutes': 15}
print(time_difference('5:30', '5:30')) # Expected Output: {'hours': 0, 'minutes': 0}