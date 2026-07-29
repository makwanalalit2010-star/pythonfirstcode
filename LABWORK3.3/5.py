'''Q.5
Convert the following:
A string '123' to an integer
A list [1, 2, 3] to a tuple
A tuple (4, 5, 6) to a list
A list of pairs [(1, 'A'), (2, 'B')] to a dictionary

'''

a = "123"
b = int(a)

print(b)
print(type(b))

lst = [1,2,3]
t = tuple(lst) 

print(t)
print(type(t))

tup = (4,5,6)
lst = list(tup)

print(lst)
print(type(lst))

pairs = [(1,'a'),(2,'b')]
d = dict(pairs)

print(d)
print(type(d))