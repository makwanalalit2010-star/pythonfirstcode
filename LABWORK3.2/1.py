'''Create a list of 5 fruits. Print the second and last fruit.

Q.1

Add "Mango" to the list. Remove the first element.

Sort the list alphabetically. Reverse it'''


fruits = ["apple","banana","orange","graps","pineapple"]


print("second fruit:",fruits[1])
print("last fruit:",fruits[-1])

fruits.append("mango")
print(fruits)

fruits.pop(0)
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)