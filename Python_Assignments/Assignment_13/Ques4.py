#Ques 4. What will be the output of the following code:

 # Function which returns a/b
# def AbyB(a , b):
# 	try:
# 		c = ((a+b) / (a-b))
# 	except ZeroDivisionError:
# 		print "a/b result in 0"
# 	else:
# 		print c

# Driver program to test above function
# AbyB(2.0, 3.0)
# AbyB(3.0, 3.0)

# Output...

# File "C:/Users/HP/PycharmProjects/Python_Assignments/Ques4.py", line 8
#     print "a/b result in 0"
#                           ^
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print("a/b result in 0")?

# After Correcting the code
#Function which returns a/b
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print("a/b result in 0")
	else:
		print(c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

#Output...

# -5.0
# a/b result in 0


