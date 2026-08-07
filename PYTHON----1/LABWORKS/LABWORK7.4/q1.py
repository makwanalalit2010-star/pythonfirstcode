'''Q.1 Write a Program to find the length of a 1D array without using any built-in function.'''


items=[]
s=int(input("enter array size: "))

print("enter array elements:")

for i in range(s):
    i=int(input(f"a[{i}]="))
    items.append(s)

count = 0

for i in items:
    count = count + 1
print("length of an array:", count)