#Create a program to find the sum of digits of a number.

num = int(input("enter a number:"))

sum = 0 

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

    print("sum of digits =", sum)