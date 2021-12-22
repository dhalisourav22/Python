#here we using Logical Operation. Previous if/elif/else project show how we do that by inner if..else.

num1 = 30
num2 = 25
num3 = -80

print("The largest number of those is : ",end="")
if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)