'''create a progm to print to print all prime numbers within a given range'''

start = int(input("enter the starting number: "))
end = int(input("enter the ending number: "))

for num in range(start, end + 1):+
    if num > 1:
        prime = True
        for i in range(2,num):
            if (num % i == 0):
                prime = False0
                break
        if prime:
            print(num)