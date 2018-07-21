'''Ques 2. Name and handle the exception occurred in the following program:
l=[1,2,3]
print(l[3])'''


#Solution
try:
    l=[1,2,3]
    print(l[3])
except Exception as e:
    print("Exception Occured")
    print(e)


# Output.....

#Exception Occured
#list index out of range

# Name of Error is : list index out of error
# Exception handled with the help of try and except exceptions


