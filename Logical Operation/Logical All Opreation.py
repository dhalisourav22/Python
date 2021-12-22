#There are Three Logical operation here. and, or & not.
a=200
b=33
c=500
#And , Or:
if a>b and c>a:
    print("Both condition's are True.")
if a>b or a>c:
    print("At least one of those condition are True.")

#Not:
x=5
print("\nThe Condition is now : ",end="")
print(not(x>3 and x<10))

