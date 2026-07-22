#Q.2
#Write a program where the user inputs a floating-point number.
#Convert this number into an integer using int().
#Print both values with a message explaining the difference.


# Input floating-point number
num = float(input("Enter a floating-point number: "))

# Convert to integer
int_num = int(num)

# Display result
print("Original Float Value:", num)
print("Converted Integer Value:", int_num)
print("int() removes the decimal part and keeps only the whole number.")