'''Ques 3. What will be the output of the following code:

# Program to depict Raising Exception

try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print
    "An exception"
    raise  # To determine whether the exception was raised or not'''


# try:
#     raise NameError("Hi there")  # Raise Error
# except NameError:
#     print
#     "An exception"
#     raise

# Output...
# Traceback (most recent call last):
#   File "C:/Users/HP/PycharmProjects/Python_Assignments/Ques3.py", line 14, in <module>
#     raise NameError("Hi there")  # Raise Error
# NameError: Hi there



# Code of removing above Error
try:
    raise NameError("Hi there")
except NameError:
    print("An Exception")


# Output...

# An Exception