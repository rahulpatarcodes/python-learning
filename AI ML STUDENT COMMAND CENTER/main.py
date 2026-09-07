while True:

    print("\n===== STUDENT COMMAND CENTER =====")
    print("1. Add Subject")
    print("2. View Subjects")
    print("3. Study Session")
    print("4. Statistics")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Add Subject selected")

    elif choice == "2":
        print("View Subjects selected")

    elif choice == "3":
        print("Study Session selected")

    elif choice == "4":
        print("Statistics selected")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
