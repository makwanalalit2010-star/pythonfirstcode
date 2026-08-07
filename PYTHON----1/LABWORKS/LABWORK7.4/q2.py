'''Q.2 Write a Program to find the average of a 1D array without using any built-in function.'''

items=[]
s=int(input("enter array size: "))
print("enter array elements:")

for i in range(s):
    v=int(input(f"a[{i}]="))
    items.append(v)

    summ=0
    for i in items:
        summ+=i
lenn=0
for i in items:
    lenn = lenn + 1
    print("average is", summ/lenn)   
     