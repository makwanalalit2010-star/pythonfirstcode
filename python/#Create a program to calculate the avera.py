#Create a program to calculate the average of N numbers entered by the user.
dig=0
a=0
for i in range(5):  # Assuming you want to enter 5 numbers
    a=int(input("enter no."))
    dig=dig+a
print("average is",dig/5)
