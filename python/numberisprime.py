#Create a program to check whether a number is a prime number.
num = int(input("enter a number:"))

for i in range(1,num):

    b=num % i == 0

if b == 2:
        print("prime number")
else:
        print("not a prime number")