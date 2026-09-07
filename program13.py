print("\n------------------EXCEPTION HANDLING--------------------------")

try:
    x=int(input("Enter a First Number:"))
    y=int(input("Enter a Second Number:"))

    result=x/y
    print("Result:", rsult)

except ValueError:
    print("Please Enter only the Number.")
except ZeroDiisionError:
    print("You cannot divide by zero")
finally:
          print("Calculation Finished.")

