'''Q.3
Create a dictionary:
student = {"name": "Alice", "age": 20, "grade": "A"}

Print the keys and values
Add a new key: "city": "Delhi"
Update "age" to 21
Delete the "grade" key

'''
student = {

    "name" : "lalit",
    "age": 20,
    "grade" : "A"

}

print("keys:", student.keys())

print("values:",student.values())

student["city"] = "delhi"

student["age"] = 21

del student["grade"]

print(student)

