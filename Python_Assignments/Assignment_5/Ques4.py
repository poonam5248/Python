'''
Ques 4. Write an if statement that lets a competitor know which of these prizes they won based on the number of points they scored, which 
is stored in the integer variable points(your input). points can only take on positive integer values up to 200. 
If they've won a prize, the message should state "Congratulations! You won a [prize name]!" with the prize name. 
If there's no prize, the message should state "Sorry! No prize this time."

Points	Prize
1-50	    No Prize
51-150	    Wooden Dog
151-180	Book
181-200	Chocolates
'''
n1=int(input("Enter a value: "))
print("\n")
print("You Entered : ",n1)
print("\n")
if n1>=1 and n1<=50:
 print("No Prize")
elif n1>50 and n1<=150:
 print("Wooden Dog") 
elif n1>150 and n1<=180:
 print("Book")
elif n1>180 and n1<=200:
 print("Chocolates") 
else:
 print("Sorry! No Prize this time.") 

