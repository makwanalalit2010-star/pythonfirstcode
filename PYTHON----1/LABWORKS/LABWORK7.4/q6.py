'''Q.6 In a user-defined array (by taking input):
Print all even numbers.
Print all odd numbers.'''

arr = []
earr = []
oarr = []

for i in range(5):
    a = int(input("enter the elements: "))
    arr.append(a)
print(arr)
for j in arr:
    if j%2==0:
        earr.append(j)
    elif j%2!=0:
        oarr.append(j)
        print(earr)
        print(oarr)
    