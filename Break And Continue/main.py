#Break statement sptop the loop.(This is must use under the loop with conditional statement)
i=0
print("Example Of Break : ",end="")
while i<10:
    i+=1
    if i==5:
        break
    print(i,end=", ")


#continue just skip the current state, which is bellow the continue statement.
i=0
print("\nExample of continue : ",end="")
while i<10:
    i+=1
    if i==5:
        continue
    print(i,end=", ")
