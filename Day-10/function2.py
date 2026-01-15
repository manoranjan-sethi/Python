# 1. write a program that accepts a string and couts the number of upper and lower case letters.

# Normal type
def upperLower(str):
    upperCounter=0
    lowerCounter=0
    for i in str:
        if i.isupper():
            upperCounter+=1
        elif i.islower():
            lowerCounter+=1
        else:
            pass

    print(f"The upper count is {upperCounter} and lower count is {lowerCounter}")

upperLower("This is APPOLO")

# using dictionary

def upperLower(str):
    dictString ={"upperCounter":0,"lowerCounter":0}
    for i in str:
        if i.isupper():
            dictString["upperCounter"]+=1
        elif i.islower():
            dictString["lowerCounter"]+=1
        else:
            pass

    print(f"The upper count is {dictString["upperCounter"]} and lower count is {dictString["lowerCounter"]}")

upperLower("This is APPOLO")

# 2. write a python function that takes a list and returns a new list with distinct elements
# i/p-> [1,2,3,3,4,4,78,78,5]
# o/p-> [1,2,3,4,78,5]

list1=[1,2,3,3,4,4,78,78,5]
uniqueList=[]
count=0

for i in list1:
    if i not in uniqueList:
            uniqueList.append(i)
            # print(i)
print(f"Unique List->{uniqueList}")

"""
Map -> eliminates the loop from the function
    -> helps in type casting answer in desired data types
    -> used while calling the function
    -> will map every value or object
    syntax-> data-type(map(function_name,iterable)) 
"""
list1=[1,2,3,3,4,4,78,78,5]

# type 1 general
def OddEven(a): 
    even=[]
    odd=[]
    for i in a:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    print(f"Even->{even} and Odd->{odd}")

OddEven(list1)

# type 2 with map

def oddEvenMap(b):
    if b%2==0:
        return "even"
    else:
        return "odd"

print(oddEvenMap(6)) #primitive

#syntax-> data-type(map(function_name,iterable)) -> Non-primitive
print(list(map(oddEvenMap,list1)))

# 3. Accept one list of strings and print the length of them in a list
listStr=["apple","papaya","guava","kiwi"] 

def length(a):
    return len(a)

print(len("ice"))

print(list(map(len,listStr)))

'''
Filter -> works same as map
       -> filter out only the values of true block
'''

def evenFilter(a):
    if a%2==0:
        return a

print(list(filter(evenFilter,list1)))

'''
Reduce -> dont need to typecast the data type
       -> minumum numbers of arguments should be 2 
'''

import functools # import is needed to use reduce function

def reduceFn(a,b):
    return a+b

print(functools.reduce(reduceFn,list1))

# Normal Sum
def totalSum(a):
    sum=0
    for i in a:
        sum+=i
    return sum

print(totalSum(list1))

# 4. Factorial of a number

def fact(a,b):
    return a*b

print(functools.reduce(fact,5))

