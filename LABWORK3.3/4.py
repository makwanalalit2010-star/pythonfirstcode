'''Q.4
Create a dictionary from two lists:
keys = ['id', 'name', 'email']
values = [101, 'Bob', 'bob@example.com']

'''


keys = ['id','name','email']
values = [101,'bob','bob@example.com']

student = {
    keys[0]: values[0],
    keys[1]: values[1],
    keys[2]: values[2]
}

print(student)