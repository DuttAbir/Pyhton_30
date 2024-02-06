
"""
    Validates a date string in the format 'dd-mm-yyyy'.
    Returns 'today', 'past', or 'future' based on the date's relation to the current date.
    Raises a ValueError for invalid dates or formats.
"""

from datetime import datetime

def validate_date(date_str):
    format="%d-%m-%Y"
    if datetime.strptime(date_str,format):
        date=datetime.today()
        dates=""
        today=date.day
        thisMonth=date.month
        thisYear=date.year

        dates = (dates.join(i  for i  in date_str if i.isnumeric()))
        day= int(dates[0:2])
        month=int(dates[2:4])
        year=int(dates[4:8])

        if day<=31 and month <=12:
            if year<thisYear:
                return "past"
            elif year>thisYear:
                return "future"
            else:
                if month<thisMonth:
                    return "past"
                elif month>thisMonth:
                    return "future"
                else:
                    if day<today:
                        return "past"
                    elif day>today:
                        return "future"
                    else:
                        return "today"
            
        else:
            raise ValueError
    else:
        raise ValueError


    
    





# Example function calls
if __name__ == '__main__':
    print(validate_date("12-11-2023"))  # Output will depend on the current date
    print(validate_date(datetime.today().strftime('%d-%m-%Y')))  # Should return 'today'
    print(validate_date("01-01-2000"))  # Should return 'past'
    print(validate_date("32-12-2023"))  # Should raise ValueError
