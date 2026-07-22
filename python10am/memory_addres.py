'''Q.5

Declares two variables with the same value.

Prints their memory addresses using id() and checks if they are the same.

Modifies one of the variables and checks the memory addresses again.'''
a = 10
b = 20

print("value of a:", a)
print("value of b:", b)

print("memory address of a:", id(a))
print("memory address of b:", id(b))

print("same memory address:", id(a) == id(b))

b = 10

print()
print("after changing b")

print("value of a:", a)
print("value of b:", b)

print("memory address of a:", id(a))
print("memory address of b:", id(b))

print("same memory address:", id(a) == id(b))