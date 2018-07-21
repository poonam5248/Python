'''Ques 2. Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a
program that determines and prints all the perfect numbers between 1 and 1000. [An integer number is said to be
“perfect number”if its factors, including 1(but not the number itself), sum to the number.
E.g., 6 is a perfect number because 6=1+2+3].'''

# Ist Method
limit = int(input("enter upper limit for perfect number search: "))

n = 1

while n <= limit:

    sum = 0
    divisor = 1
    while divisor < n:
        if not n % divisor:
            sum += divisor
        divisor = divisor + 1
    if sum == n:
        print(n, "is a perfect number")
    n = n + 1
# 2nd Method
'''def perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum = sum + i
    if sum == n:
        return True
    else:
        return False


 for i in range(1, 1001):
        if perfect(i):
            print(i)'''



