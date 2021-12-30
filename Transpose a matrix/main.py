x =[[2,7],
    [4,5],
    [3,8]]

transposeMatrix = [[0,0,0],
                   [0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        transposeMatrix[j][i] = x[i][j]         #the change will happen there.

print("After Transpose The Matrix : ")
for i in range(len(transposeMatrix)):
    for j in range(len(transposeMatrix[0])):
        print(transposeMatrix[i][j],end="     ")
    print()