'''
         create a function named calculate_age that calculates a person's age in years, months, and days. 
         The function will take a single argument: the person's date of birth in the string format dd-mm-yyyy.
         Your function should return a dictionary containing three keys: years, months, and days. 
         Each key should map to an integer representing the respective part of the age calculated.

'''
from datetime import datetime

def calculate_age(dob_str):
    today=datetime.today()
    if datetime.strptime(dob_str,"%d-%m-%Y" ):
        DOB = datetime.strptime(dob_str, "%d-%m-%Y").date()

        try:

            if DOB.year>today.year or (DOB.year==today.year and DOB.month>today.month) or (DOB.year==today.year and DOB.month>today.month and DOB.day>today.day):
                raise ValueError
            
            else:

                age_years = today.year-DOB.year


                #if today.month<DOB.month or (today.month==DOB.month and today.day < DOB.day):
                    #age_years-=1

                age_month=today.month-DOB.month
                age_days=today.day-DOB.day

                if age_month<0 or (age_month == 0 and age_days < 0):
                    age_years-=1
                    age_month+=12

                
                if age_days<0:
                    '''age_month-=1
                    age_days+=30'''

                    age_days += (datetime(today.year, today.month, 1) - datetime(today.year, today.month-1, 1)).days

                for years in range(DOB.year, today.year if today.month<3 else today.year+1):
                    if years%4==0:
                        age_days+=1

                if age_days>30:
                    age_month+=1
                    age_days-=30

                return({'years': age_years, 'months': age_month, 'days': age_days })
        except ValueError:
            return("Date of birth has not occured yet")
    else:
        raise ValueError



# Example function calls
print(calculate_age("01-01-2010"))  # Example of a past date
print(calculate_age(datetime.today().strftime("%d-%m-%Y")))  # Example of the current date
print(calculate_age(datetime.strftime(datetime.today().replace(year=datetime.today().year, day=1, month=6 ), '%d-%m-%Y')))  # Example of the current year date
print(calculate_age("15-06-2021"))  # Example of a date within the last year










