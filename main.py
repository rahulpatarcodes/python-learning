print("==============================================")
print("     AI/ML STUDENT COMMAND CENTER         ")
print("==============================================")

while True:
    print("\n1. Add Subject")
    print("2. View Subjects")
    print("3. Study Session")
    print("4. Add Marks")
    print("5. Statistics")
    print("6. Save data")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Add Subject selected")

    elif choice == "2":
        print("View Subjects selected")

    elif choice == "3":
        print("Study Session selected")

    elif choice == "4":
        print("Add Marks selected")

    elif choice == "5":
        print("Statistics selected")
    elif choice == "6":
        print("Save Data selected")
    elif choice == "7":
        print("Goodbye !")
        break

    else:
        print("Invalid choice")
