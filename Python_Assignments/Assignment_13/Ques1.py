'''Ques 1. Name and handle the exception occured in the following program:

a=3
 if a<4:
    a=a/(a-3)
     print(a)'''


#Solution

try:
    a=3
    if a<4:
        a=a/(a-3)
        print(a)
except Exception as e:
    print("Exception Occured")
    print(e)

# Output.....

#Exception Occured
#division by error

# Name Of error is : divion by zero error
# Exception handled with the help of try and except exceptions


