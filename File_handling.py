print("\n-------FILE HANDLING-----------------")

try:
    with open("Student.txt", "w") as file:
        file.write("Course: CSE AI/ML")
        file.write(" Marks:20")
        file.write(" Grade:E")
    print("Data Saved Successfully.")

    with open("Student.txt", "r") as file:
        data=file.read()

    print("------ FILE CONTENT-----------")
    print(data)

except Exception as error:


    print("Something went wrong:", error)
