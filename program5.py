print("\n---- FOR LOOP ---")
for i in range(1,6):
    print("Number:", i)


print("\n--- WHILE LOOP ----")
counter = 1
while counter <=3:
    print("Counter:", counter)
    counter +=1

print("\n--- BREAK / CONTINUE ---")

for number in range(1,11):
    if number ==5:
        continue
    if number ==9:
        break
    print(number)
