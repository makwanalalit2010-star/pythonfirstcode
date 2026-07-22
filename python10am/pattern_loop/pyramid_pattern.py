'''for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

'''

n=5
for i in range(n,0,-1):
    for j in range(1,i):
        print(" ", end="")
        for k in range(0,n-i+1):
            print("*", end="")
        for p in range(0,n-i):
            print("*", end="")
            print("")
            