
def count_hours(day):
    total_hours=24
    if day>0:
        return f'Total hours in {day} day are {total_hours*day}'
    elif day==0:
        return "Total hours in 0 day is 0"
    else:
        return "Invalid input"

days=int(input("Enter number of days: "))
print(count_hours(days))


