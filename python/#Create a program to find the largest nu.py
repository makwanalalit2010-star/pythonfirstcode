#Create a program to find the largest number from a list of numbers using a loop.
b=[]
for i in range(9):  # Assuming you want to enter 5 numbers
    a=int(input("enter no."))
    b.append(a)
print("max no is",max(b))

