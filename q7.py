<<<<<<< HEAD
'''Write a program to demonstrate assignment operators (=, +=, -=, *=, /=) using a single variable.'''

num = 10
print("initial value:", num)

num += 6
print("after +=6:", num)

num -= 2

print("after -=2:", num)

num *= 3
print("after *=3:", num)

num /= 4
print("after /=4:", num)
=======
'''Check if a string starts with "Hello" and ends with "World"

-Remove all non-alphabetic characters from "Data123@Science!"

Reverse the string "Python"'''

text = input("enter a string:")

print("start with 'hello':",text.startswith("hello"))
print("ends with 'world':",text.endswith("world"))

text2 = "Data123@Science!"
result = ""

for ch in text2:
    if ch.isalpha():
        result += ch

print("original string:",text2)
print("after removing non-alphabetic characters:",result)

word = "python"
reverse = word[::-1]

print("reversed string:",reverse)
>>>>>>> 9654e5201c5ca4bc3a69745dd3835bd07e3d6410
