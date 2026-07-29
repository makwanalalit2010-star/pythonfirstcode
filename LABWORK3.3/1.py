'''Q.1
Create a set of integers: {1, 2, 3, 4, 5}.
Add 6, remove 3, and check if 2 is in the set.

'''


num = {1,2,3,4,5}

num.add(6)
num.remove(3)

print(num)

if 2 in num:
    print("2 in set")
else:
    print("2 is not in set")

