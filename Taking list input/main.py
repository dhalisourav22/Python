#input a general list from user.
amountOfItem = int(input("Enter the number of item you have : "))
demoList = []

for x in range(amountOfItem):
    print(f"Please Enter your {x} index list item :",end=" ")
    demoList.append(input())

print("\nAfter finish taking input :",demoList)