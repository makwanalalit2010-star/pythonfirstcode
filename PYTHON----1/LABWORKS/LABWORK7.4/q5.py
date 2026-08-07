'''Q.5 Take user input for a number.
Check if it exists in the array.
Print the index if found, else print "Not Found".'''


# arr = [10,20,30,40,50]

# x = int(input("enter number: "))

# if x in arr:
#     print("index =",arr.index(x))
# else:
#     print("not found")
arr=[]
for i in range(5):
    a=int(input("enter the elements: "))
    arr.append(a)
print(arr)
b=int(input("enter the element to find :"))
if b in arr:
    print("element found and its index is ",arr.index(b))
else:
    print("element not found")
