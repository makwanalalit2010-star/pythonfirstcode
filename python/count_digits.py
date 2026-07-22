#Create a program to count the number of digits in a given number.

number = int(input("enter a number:"))

count = 0

while number > 0:

    number = number // 10
    count = count + 1

print("the number of digits =" , count)