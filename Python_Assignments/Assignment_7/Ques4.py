# Ques 4. Write a function to calculate power of a number raised to other ( a^b ) using recursion.


def power(a,b):
  if b == 1:
    return a
  else:
    return a*power(a,b-1)
print ("Power of number is:",power(48,2))
print ("Power of number is:",power(52,2))
print ("Power of number is:",power(100,2))