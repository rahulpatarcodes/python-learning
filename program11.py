print("\n-------------FUNCTIONS----------------------")
m1=int(input("Enter the First Number:"))
m2=int(input("Enter the Second Number:"))
m3=int(input("Enter the Third Number:"))


def calculate_average(m1,m2,m3):
    average =(m1 + m2 + m3)/3
    return average

name = input("Enter your name: ")
def greet(usrname="Student"):
    return f"Welcome, {name}!"

average = calculate_average(m1,m2,m3)

print(greet(name))
print("Average:", average)

# ------------------------------------------------------------------------------
