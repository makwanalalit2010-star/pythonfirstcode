<<<<<<< HEAD
'''Implement a program to demonstrate logical operators (and, or, not) by asking the user for boolean inputs (e.g., true/false values).'''

bool1 = input("enter a bool value (true/false): ")
bool2 = input("enter another bool value (true/false):")

print("bool1 and bool2:", bool1 and bool2)
print("bool1 or bool2:", bool1 or bool2)
print("not bool1:", not bool1)
print("not bool2:", not bool2)

=======
'''Split "apple,banana grapes" into a list

Join the list ["Python", "is", "awesome"] into a sentence using spaces.

Split a multiline string into separate lines and print them one by one.'''

fruits = "apple,banana,grapes"
fruit_list = fruits.split(",")

print("fruit_list:",fruit_list)

word = ["python","is","awesome"]
sentence = " ".join(word)
print("joined sentence:",sentence)

text = """welcome to python learning strings have a nice day"""

lines = text.splitlines()

print("lines:")
for line in lines:
    print(line)
>>>>>>> 9654e5201c5ca4bc3a69745dd3835bd07e3d6410
