# Sets accept only unique values and are unordered collections

set_month= {'January', 'February', 'March', 'April'}

for month in set_month:
    print(month)

print(type(set_month))  # <class 'set'>

set_month.add('May')
print(set_month)

set_month.add('March')
print(set_month)      # No effect as 'March' already exists

set_month.remove('February')
print(set_month)

# if we want to remove an duplicate item from list the first occurrence only is removed
list_month= ['January', 'February', 'March', 'April', 'March']
list_month.remove('March')
print(list_month)   # ['January', 'February', 'April', 'March']