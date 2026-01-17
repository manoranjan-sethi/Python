import datetime

user_input = input("Enter a deadline date (DD-MM-YYYY): ")  # ex - Learn Python:25.01.2026
input_list = user_input.split(':')


goal = input_list[0]  # Deadline date string
deadline = input_list[1]

deadline_date =datetime.datetime.strptime(deadline, '%d.%m.%Y')  # Converting string to date object
today=datetime.datetime.now()  # Current date and time


# Calculate the date from today to deadline date

time_left=deadline_date-today
hours_left=int(time_left.total_seconds()/3600)

print(f'Time left to complete your goal "{goal}" is {time_left.days} days left')
print(f'Time left to complete your goal "{goal}" is {hours_left} hours left')