'''Create a program to check whether a number is divisible by both 5 and 11'''

num = int(input("enter a number:"))

if num % 5 == 0 and num % 11 == 0:
    print("entered number is divisible by both 5 and 11:")
else:
    print("entered number is not divisible by both 5 and 11:")
    