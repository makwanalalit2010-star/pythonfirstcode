#Create a program to calculate the power of a number using a loop.


#a = int(input("enter a number:"))
#b = int(input("enter the power:"))

#print(a**b)

n = int(input("Enter number: "))
p = int(input("Enter power: "))

ans = 1

for i in range(p):
    ans = ans * n

print(ans)