'''Ques 5. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will 
cost 100. Judge and print total cost for user.'''

qty=int(input("Enter Quantity: "))

totalexp=qty*100
if totalexp>1000:
 dis=totalexp*0.1
 totalexp=totalexp-dis
 print("Cost is %d " %totalexp)
else: 
 print("Total cost is %d "%totalexp) 
