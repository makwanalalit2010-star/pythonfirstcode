#Create a program to calculate the electricity bill based on different unit ranges.

units = float(input("enter the number of units consumed:"))

if units <= 100:
     bill = units *  1.5
elif units <= 200:
     bill = (100*5) + ((units - 100) * 2.5)
else:
     bill = (100*5) + (100*2.5) + ((units - 200) * 4)

print("the electricity bill is:", bill)