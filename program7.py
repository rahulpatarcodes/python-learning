print("\n------LISTS----------")
subjects =[
    "Mathematics",
    "Physics",
    "Electrical",
    "Python"
]
print("Subjects:", subjects)
print("First Subjects:", subjects[0])

subjects.append("AI")
subjects.insert(1,"Programming")

print("After adding:", subjects)

subjects.remove("Physics")
print("After removing Physics:", subjects)
print("Number if subjects:", len(subjects))
