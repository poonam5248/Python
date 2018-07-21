# Ques 4. Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

s=raw_input()
d={ "UPPER_CASE" :0,  "LOWER_CASE" :0}
for c in s:
    if c.isupper():
	    d[ "UPPER_CASE" ]+=1
	elif c.islower():
        d[ "LOWER_CASE" ]+=1
    else:
        pass
print("UPPER CASE: ",d[ "UPPER_CASE" ])
print("LOWER CASE: ",d[ "LOWER_CASE" ])		