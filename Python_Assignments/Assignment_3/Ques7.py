# Ques 7. Count even and odd number in a list.

l=[1,2,3,4,5,6,7,8,9,10,48,52,100,23,26,57,79,80]
even_count=0
odd_count=0
for x in l:
 if x%2==0:
  even_count=even_count+1
  
 else:
  odd_count=odd_count+1
print("Total No. of even no. in list= ",even_count)
print("Total No. of odd no. in list= ",odd_count)
