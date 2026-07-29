students = []
subjects_set = set()

print("===================================")
print(" Welcome to Student Data Organizer ")
print("===================================")

while True:
    print("\nMenu")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display Subjects")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        sid = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        grade = input("Enter Grade: ")
        dob = input("Enter Date of Birth (YYYY-MM-DD): ")

        sub = input("Enter Subjects (comma separated): ")
        subjects = [i.strip() for i in sub.split(",")]

        student_tuple = (sid, dob)

        student = {
            "id": student_tuple[0],
            "dob": student_tuple[1],
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects
        }

        students.append(student)

        for i in subjects:
            subjects_set.add(i)

        print(f"\n{name} added successfully.")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\n----- Student Records -----")
            for s in students:
                print(f"ID : {s['id']}")
                print(f"Name : {s['name']}")
                print(f"Age : {s['age']}")
                print(f"Grade : {s['grade']}")
                print(f"DOB : {s['dob']}")
                print(f"Subjects : {', '.join(s['subjects'])}")
                print("---------------------------")

    elif choice == "3":
        sid = input("Enter Student ID to Update: ")

        found = False

        for s in students:
            if s["id"] == sid:
                found = True

                s["age"] = int(input("Enter New Age: "))
                s["grade"] = input("Enter New Grade: ")

                sub = input("Enter New Subjects (comma separated): ")
                s["subjects"] = [i.strip() for i in sub.split(",")]

                subjects_set.clear()

                for stu in students:
                    for x in stu["subjects"]:
                        subjects_set.add(x)

                print("Student Updated Successfully.")
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        sid = input("Enter Student ID to Delete: ")

        found = False

        for i in range(len(students)):
            if students[i]["id"] == sid:
                del students[i]
                found = True

                subjects_set.clear()

                for stu in students:
                    for x in stu["subjects"]:
                        subjects_set.add(x)

                print("Student Deleted Successfully.")
                break

        if not found:
            print("Student not found.")

    elif choice == "5":
        print("\nUnique Subjects Offered:")
        for s in subjects_set:
            print(s)

    elif choice == "6":
        print("Thank you for using Student Data Organizer.")
        break

    else:
        print("Invalid Choice.")