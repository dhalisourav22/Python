#if..else :
a=20
b=30
print(a) if a>b else print(b)
#storig value in variable then printing this variable.
max = a if a>b else b
print("The Maximum Value is :",max)


#if..elif..else
a=2
b=2
print("\n\nThey are : ",end="")
print(a) if a>b else print("=") if a==b else print(b)


#if(Not Ternary Operation)
a=2
b=1
if a>b: print("\n\nA is bigger then B.")   #This is not ternary operation. This is show how we can read ar single statement with if/elif/else.