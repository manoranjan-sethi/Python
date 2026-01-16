def calculate_hours_try(day):
    try:
        day=int(day)
        total_hours=24
        if day>0:
            return (f'Total hours in {day} day are {total_hours*day}')
        elif day==0:
            return ("Total hours in 0 day is 0")
        else:
            return ("Please enter a valid positive integer not NEGATIVE")
    except ValueError:
        return ("Please enter a valid positive integer")