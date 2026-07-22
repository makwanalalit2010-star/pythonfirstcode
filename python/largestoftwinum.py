#Create a program to find the largest of two numbers.//

num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))

if num1>num2:
    print(num1,"is the largest number")
elif num2>num1:
    print(num2,"is the largest number")
else:
    print("both numbers are equal")