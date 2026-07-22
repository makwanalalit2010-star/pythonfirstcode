#Q.1
#Write a Python program to demonstrate the use of type casting constructors (int(), float(), str(), and bool()):
#Take input from the user as a string.
#Convert the string into an integer, a float, and a boolean.
#Print the converted values along with their types.


# Take input as string
value = input("Enter a value: ")

# Type casting
int_value = int(value)
float_value = float(value)
str_value = str(value)
bool_value = bool(value)

# Print values and their types
print("Integer:", int_value, "Type:", type(int_value))
print("Float:", float_value, "Type:", type(float_value))
print("String:", str_value, "Type:", type(str_value))
print("Boolean:", bool_value, "Type:", type(bool_value))