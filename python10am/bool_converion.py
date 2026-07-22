#takes a bool value(true or false) as input converts the bool to an int and a string,and prints all three values.

bool_value  = input("enter true or false:") == "true"

int_value = int(bool_value)
str_value = str(bool_value)

print("boolean:", bool_value)
print("integer:", int_value)
print("string:", str_value)