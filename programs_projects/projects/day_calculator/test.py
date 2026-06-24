def month_days(month, year):
    """Check the Respective Days of a month"""
    if month > 12 or month < 1:
        return 0
        
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month == 2:
        return days_in_february(year)
    else:
        return 0

def days_in_february(year):
    """Check for the Leap Year"""
    return 29 if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) else 28

def calculate_date_difference(date1, date2): 
    """Calculate the difference between Two Dates"""

    # if int(date1.split("-")[0]) < int(date2.split("-")[0]):
    #     temp_date = date1
    #     date1 = date2
    #     date2 = temp_date

    if not (1 <= int(date1.split("-")[1]) <= 12):
        return f"[{date1}]: Month should be in between 1 to 12."

    if not (1 <= int(date2.split("-")[1]) <= 12):
        return f"[{date2}]: Month should be in between 1 to 12."

    date1_split = date1.split("-")
    date1_year = int(date1_split[0])
    date1_month = int(date1_split[1])
    date1_date = int(date1_split[2])

    date2_split = date2.split("-")
    date2_year = int(date2_split[0])
    date2_month = int(date2_split[1])
    date2_date = int(date2_split[2])



    if date2_date > date1_date:
        date1_month -= 1
        if date1_month == 0:
            date1_month = 12
            date1_year -= 1
            
        date1_date += month_days(date1_month, date1_year)

    if date2_month > date1_month:
        date1_year -= 1
        date1_month += 12

    diff_day = date1_date - date2_date
    diff_month = date1_month - date2_month
    diff_year = date1_year - date2_year
    return f"{diff_year} years,  {diff_month} months, {diff_day} days"


from_date = '2026-16-22'
to_date = '1994-7-27'

# from_date = input("From Date: ")
# to_date = input("To Date: ")





print(calculate_date_difference(from_date, to_date))
