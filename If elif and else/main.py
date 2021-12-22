#if/elif/else
a=int(input("Enter The Value Of A : "))
b=int(input("Enter The Value Of B : "))

if a<b:
    print("B is grater then A.")
elif b<a:
    print("A is grater then B.")
#elif b<a: print("A is grater then B.")   #we can write this way because this elif has only one statement.
else:
    print("A and B both are equal.")


#Inner If..else
num1 = 20
num2 = -80
num3 = 40
print("\n\nThe Largest Number Of Those is : ",end="")
if num1>num2:
    if num1>num3:
        print(num1)
    else:
        print(num3)
else:
    if num2>num3:
        print(num2)
    else:
        print(num3)
