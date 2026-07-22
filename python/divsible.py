#Create a program to check whether a number is divisible by both 5 and 11.

number = int(input("enter a number:"))

if number % 5 == 0 and number % 11 == 0:
    print("the number is divisible by both 5 and 11.")

else:
    print("the number is not divisible by both 5 and 11.")