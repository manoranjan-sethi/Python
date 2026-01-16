import helper    

# if we want to export a single function we can do like this
# from helper import calculate_hours_try

days=''  # initialize days variable as it cant be undefined
while days!= 'exit': 
    days=input("Enter number of days with comma seperated list: ")
    for day in days.split(','):           # for list of inputs separated by comma
        print(helper.calculate_hours_try(day))

print("------------------------------------")

# OR


# if we want to export a single function we can do like this
from helper import calculate_hours_try

days=''  # initialize days variable as it cant be undefined
while days!= 'exit': 
    days=input("Enter number of days with comma seperated list: ")
    for day in days.split(','):           # for list of inputs separated by comma
        print(calculate_hours_try(day))