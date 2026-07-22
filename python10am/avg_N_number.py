num = int(input("enter how many numbers:"))

count = 1
total = 0

while count <= num:
    num = int(input("enter the number:"))
    total += num
    count += 1
 
average = total / num
print("the sum of the numbers is:", total)
print("the average of the numbers is:", average)