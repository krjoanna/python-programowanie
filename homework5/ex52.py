# Create the function print_working_days(date1, date2), where 'date1' and 'date2' 
#are strings of the form 'YYYY-MM-DD'. The function prints dates of working days 
#(from Monday to Friday) in the given range, 'date2' is excluded.

from datetime import timedelta
import datetime

def print_working_days(date1, date2):

    startdate = datetime.date.fromisoformat(date1) #str --> date format
    enddate = datetime.date.fromisoformat(date2) 

    numberofdays = (enddate - startdate).days       #number of days 

    for single_date in (startdate + timedelta(i) for i in range(numberofdays)):
        if single_date.weekday() in range(0, 5):                                   #check if the day is working day
            print(single_date)

#test
print_working_days("2023-04-03", "2023-09-13")