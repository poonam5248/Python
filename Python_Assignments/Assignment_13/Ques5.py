'''Ques 5. Write a program to show and handle following exceptions:
1. Import Error
2. Value Error
3. Index Error'''

#Import Error
# try:
#     import sys
#     import gw_utility.Book
# except Exception as e:
#     print(e)
# Output....
# No module named 'gw_utility'


# 2. value error

# try:
#     n1=int("Poonam")
# except Exception as e:
#     print(e)

try:
    int("Poonam")
except ValueError as e:
    print(e)


# Output...
# invalid literal for int() with base 10: 'Poonam'


#  3. Index error
#
# try:
#     l = [1, 2, 3]
#     print(l[10])
# except Exception as e:
#     print(e)

# Output....
# list index out of range
