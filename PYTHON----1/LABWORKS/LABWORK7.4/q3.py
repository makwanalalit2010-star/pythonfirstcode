'''Q.3 Write a Program to perform the addition operation of two 1D arrays & store it in another array. (Both array sizes must be the same.)'''

n = int(input("enter array size: "))

a=[]
b=[]
c=[]

print("enter array A elements: ")

for i in range(n):
    x = int(input(f"a[{i}] = "))
    a.append(x)

    print("enter array B elements:")
    for i in range(n):
        x = int(input(f"b[{i}] = "))
        b.append(x)
for i in range(n):
    c.append(a[i] + b[i])

print("array c :", c)