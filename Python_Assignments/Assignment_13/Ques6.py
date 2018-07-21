'''Ques 6. Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less
than 18. The code must keep taking input till the user enters the appropriate age number(less than 18).'''

class AgeTooSmallError(Exception):
    pass
age=0

while age<18:
    age = int(input("Enter your age: " ))
    try:
        if age<18:
            raise AgeTooSmallError("Age Too Small Exception")
    except Exception as e:
        print(e)
    else:
        print("No Exception")