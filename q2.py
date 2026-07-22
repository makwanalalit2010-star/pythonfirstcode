<<<<<<< HEAD
'''Create a program that asks the user for their name, age, and favourite hobby using the input() function, then displays a formatted message like: - "Hello, <name>! At <age>, enjoying <hobby> sounds fun!"'''

name = input("enter your name: ")
age = input("enter your age: ")
hobby = input("enter your favourite hobby: ")
print("Hello", name + "!", "At", age + ",", "enjoying", hobby, "sounds fun!")
=======
'''Q.2

Create a program to:

- Format and display the following sentence: "The price of (item) is (price) dollars."

- Replace (item) with "apple" and (price) with 5.50 using f-strings.'''
'''
item=input("enter the name of the item :")
price=input("entr the price of the item :")
a=f"the price of {item} is {price} dollars"
print(a)
b=a.split()
b[3]="apple"
b[5]="5.50"
print(" ".join(b))'''

item = "apple"
price = 5.50

print(f"the price of {item} is {price} dollars.")
print(f"the price of {item} is {price:.2f} dollars.")


>>>>>>> 9654e5201c5ca4bc3a69745dd3835bd07e3d6410

