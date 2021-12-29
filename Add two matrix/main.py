#Ading Two Matrix.
x=[[1,2,3],[4,5,6],[7,8,9]]
y=[[11,12,13],[14,15,16],[17,18,19]]

z=[[0,0,0],[0,0,0],[0,0,0]]        #Store Here the answer.

for rowIndex in range(len(x)):
    for colIndex in range(len(x[0])):
        z[rowIndex][colIndex] = x[rowIndex][colIndex]+y[rowIndex][colIndex]

print("The Matrix Is : ")
for row in z:
    for col in row:
        print(col,end="   ")
    print()