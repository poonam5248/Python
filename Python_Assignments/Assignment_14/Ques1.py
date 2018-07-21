# Ques 1. Write a Python program to read last n lines of a file.


f=open('Textfile.txt','r',encoding="utf8")
content=f.readlines()
n=int(input("Enter Number of lines You want to read From last :"))

while n>0:
    print(content[-n])
    n-=1

f.close()