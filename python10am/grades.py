'''Create a program to assign grades based on marks entered by the user.'''
marks = int(input("enter your marks:"))

if marks >=90:
    print("your grade is a:")
elif marks >=80:
    print("your grade is b:")
elif marks >=70:
    print("your grade is c:")
elif marks >=60:
    print("your grade is d:")
elif marks >=35:
    print("grade e:")
else:
    print("grade: f(fail)")
    