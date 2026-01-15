# Try Except Block to catch the error and tell what to do with the error. 
# Better to have this instead of nested if else

def calculate_hours_try(days):
    try:
        days=int(days)
        total_hours=24
        if days>0:
            return (f'Total hours in {days} day are {total_hours*days}')
        elif days==0:
            return ("Total hours in 0 day is 0")
        else:
            return ("Please enter a valid positive integer not NEGATIVE")
    except ValueError:
        return ("Please enter a valid positive integer")

days=''  # initialize days variable as it cant be undefined
while days!= 'exit': 
    days=input("Enter number of days: ")
    print(calculate_hours_try(days))