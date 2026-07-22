#Create a program to reverse a number using a loop.

num = int(input("enter a number:"))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

    print("the reverse of the number is =", reverse)
    