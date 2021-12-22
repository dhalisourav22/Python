#The else clause executes after the loop completes normally. This means that the loop did not encounter a break state ment.

#Example 1 (Abnormal stoping.) :
i=0
print("Example No 1 : ",end="")
while i<10:
    i+=1
    if i==5:
        break
    print(i,end=", ")
else:
    print("\nThis is Else.\n")


#Example 2(This is normal stoping.) :
i=0
print("\n\nExample No 2 : ",end="")
while i<10:
    i+=1
    if i==5:
        continue
    print(i,end=", ")
else:
    print("\nThis is Else.\n")


#Example 3 (normal stoping. Because Here break statement never read.) :
i=0
print("Example No 3 : ",end="")
while i<10:
    i+=1
    if i==18:
        break
    print(i,end=", ")
else:
    print("\nThis is Else.\n")


#Example 4(This While loop never be executed.) :
i=0
print("Example No 4 : ",end="")
while i<-10:
    i+=1
    print(i,end=", ")
else:
    print("\nThis is Else.\n")