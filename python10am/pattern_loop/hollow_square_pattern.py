for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)

for i in range(4, 0, -1):
    print(" " * (5 - i) + "* " * i)'''

'''for i in range(1, 6):
    for j in range(1, 11):
        print(i * j, end="\t")
    print()
'''