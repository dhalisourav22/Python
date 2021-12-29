#input a matrix means a 2D list.
row = int(input("Enter the number of Row : "))
col = int(input("Enter the number of Column : "))

outerList =[]
print("\nEnter Your Matrix : ")
for i in range(row):
    innerList = []
    for j in range(col):
        innerList.append(int(input(f"\t\t\t\t\tEnter the ({i+1},{j+1}) index item : ")))          #here the item are in integer data type. because a matrix should be in integer data type or float data type.
    outerList.append(innerList)

print("\nThe Matrix is : ")
for rows in outerList:
    for cols in rows:
        print(cols,end="    ")
    print()
