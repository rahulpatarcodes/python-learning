print("\n------DICTIONARY------")

name=(input("Enter the Student Name:"))
age=int(input("Enter the age of the Student:"))
marks=int(input("Enter the marks of the student"))
student = {
    "Name:", name,
    "age:", age,
    "marks:", marks,
    "course:", "CSE AI?ML"
}

print("Student:", student)

print("Name:",name)
print("Marks:",marks)

student["semester"] = 1

for key, value in student.items():
    print(key, ":", value)
