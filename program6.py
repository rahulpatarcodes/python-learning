print("\n------- STRINGS--------")

course="Python Programing"
print("String:",course)
print("First Character:",course[0])
print("Last Character:",course[-1])
print("First 6 Character:", course[:-6])
print("Length:", len(course))
print("Upper:", course.upper())
print("Lower:", course.lower())
print("Replace", course.replace("Python", "AI"))

if "Python" in course:
    print("Python found !")
