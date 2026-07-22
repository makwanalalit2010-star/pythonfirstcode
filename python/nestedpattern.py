#Create a program to print different star patterns using nested loops.
x=0
y=0

for x  in range(5):
    for y  in range(x+1):
        print("*", end="")
    print()