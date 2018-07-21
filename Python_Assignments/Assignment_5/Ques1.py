# Ques 1. Take an input year from user and decide whether it is a leap year or not.

year=int(input("Enter any Year: "))

if (year%4)==0:
 if (year%100)==0:
  if (year%400)==0:
   print("{0} is a leap year".format(year))
  else:
   print("{0} is not a leap year ".format(year))
 else:
  print("{0} is a leap year".format(year))
else:
 print("{0} is not a leap year".format(year))    
    