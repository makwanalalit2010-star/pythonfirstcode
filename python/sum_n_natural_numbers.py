#Create a program to calculate the sum of the first N natural numbers.

n = int(input("Enter a number: "))

sum = 0

for i in range(1, n + 1):
    sum = sum + i

print("Sum =", sum)