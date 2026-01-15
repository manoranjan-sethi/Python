
def count_hours(days):
    total_hours=24
    if days>0:
        return f'Total hours in {days} day are {total_hours*days}'
    elif days==0:
        return "Total hours in 0 day is 0"

def validate_input(days):     # clearner function to validate input
    if days.isdigit():
        days=int(days)
        print(count_hours(days))
    else:
        print("Please enter a valid positive integer")

days=input("Enter number of days: ")
validate_input(days)

# To consdolidate this in a single function, we can do the following:

def calculate_hours():
    days=input("Enter number of days: ")
    if days.isdigit():
        days=int(days)
        total_hours=24
        if days>0:
            return (f'Total hours in {days} day are {total_hours*days}')
        else:
            return ("Total hours in 0 day is 0")
    else:
        return ("Please enter a valid positive integer")

print(calculate_hours())
