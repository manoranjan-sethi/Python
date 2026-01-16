import datetime

user_input = input("Enter a deadline date (DD-MM-YYYY): ")
input_list = user_input.split(':')


goal = input_list[0]  # Deadline date string
deadline = input_list[1]
