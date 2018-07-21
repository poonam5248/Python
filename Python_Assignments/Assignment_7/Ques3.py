# Ques 3. Print multiplication table of 12 using recursion.


def table(n,i):
  print ("%d*%d=%d"% (n,i,n*i))
  i=i+1
  if i<=10:
    table(n,i)
table(12,1)






