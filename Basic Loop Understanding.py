'''Level 1: Basic Loop Understanding'''

'''1. Print numbers from **1 to 20** using a loop. '''

for i in range(1,21):
    print(i)

'''2. Print Numbers from 20 to 1 (Reverse Order)'''

for i in range(20,0,-1):
    print(i)

'''3. Print All Even Numbers Between 1 to 50'''

for i in range(2,51,2):
    print(i)

'''4. Print All Odd Numbers Between 1 to 50'''

for i in range(1,51,2):
    print(i)

'''5. Print Numbers from 1 to n (Take n from User)'''

n = int(input("enter a number:"))

for i in range(1,n+1):
    print(i)

'''🔹 Level 2: Loop + Conditions'''

'''1. Print Numbers from 1 to 100 that are Divisible by 3'''

for i in range(1,101):
    if i % 3 == 0:
        print(i)

'''2. Print Numbers from 1 to 100 that are Divisible by Both 3 and 5'''

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

'''3. Count How Many Numbers Between 1 to 50 are Even'''

count = 0 

for i in range(1,51):
    if i % 2 == 0:
        count = count + 1
    print("total even num",count)

'''4. Take a Number and Count How Many Numbers from 1 to n are Divisible by 7'''

num = int(input("enter a number:"))

count = 0
for i in range(1, n + 1):
    if i 5 7 == 0:
count = count + 1


print("number divisible by 7 ",count)

