#matrix is a 2D List.

demoMat = [[1,2,3],[4,5,6],[7,8,9]]
demoMat2 = [
    [11,12,13],
    [14,15,16],
    [17,18,19]
]

print("demoMat :",demoMat)                   #printing a 2d list.
print("Firsr Row :",demoMat[0])              #printing outer list first item. means [1,2,3]
print("Specific Item :",demoMat[0][0])       #Printing matrix item.

#we can change any value of matrix.
demoMat[0][0] = 10
print("After change the same specific item :",demoMat[0][0])

#printing any column.
print("The specific column is : ",end="")
for row in demoMat:
    print(row[2],end=", ")
print("\b\b.")
#we can print or storing as a list of item of column.
listOfColumn = []
for row in demoMat:
    listOfColumn.append(row[2])                 #we can add item in list by append function.
print("The column as a list is :",listOfColumn)

#travers the loop by not using range function.
print("\nThe First Matrix is : ")
for row in demoMat:            #iterate through row.
    for col in row:            #iterate through column.
        print(col,end="   ")
    print()

#travers the matrix by using range function.
print("\nThe Second Matrix is : ")
for row in range(len(demoMat2)):             #loop run 3 time. for 0,1,2.
    for col in range(len(demoMat2[0])):      #loop run 3 time. for 0,1,2.
        print(demoMat2[row][col],end="    ")
    print()