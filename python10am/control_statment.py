'''english = 24
maths = 16
science = 26
total = english + maths + science

if total >= 60:

if (english >= 20 and maths >= 20 and science >= 20):

print(pass)

else:
print(Fail)'''

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")

