''' Ques 1. Extract the user id, domain name and suffix from the following email addresses. 
emails = "zuck26@facebook.com" , "page33@google.com" , "jeff42@amazon.com"
desired_output = [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')] '''



import re
email_1="zuck26@facebook.com"
email_2="page33@google.com"
email_3="jeff42@amazon.com"
p=re.compile(r"([a-zA-Z0-9]+)@([a-zA-Z]+).([a-z]+)")
def display(email):
    result=p.match(email)
    print(result[1],end=" ")
    print(result[2],end=" ")
    print(result[3])
display(email_1)
display(email_2)
display(email_3)
