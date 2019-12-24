import numpy as np

def setZeros (matrix):
    row = [0]* len(matrix)
    column = [0] * len(matrix[0])
    print (len(matrix))
    #Store the row and column index with value 0
    for i in range (len(matrix)):
        for j in range (len(matrix[0])):
            if matrix[i][j] == 0:
                row[i] = 1
                column[j] = 1
    print (row)
    print(column)
    #Set arr[i][j] to 0 if either row i or column j has a 0
    for i in  range (len(matrix)):
        for j in range (len(matrix[0])):
            if row[i] == 1 or column[j] == 1:
                matrix[i][j] = 0;

def printMatrix (M, n):
    print(np.matrix(M))

A = [[1, 4, 5, 6],
    [-5, 8, 0, 7],
    [0, 1, 2, 3],
    [9, 3, 4, 7]]
printMatrix(A, 4)
setZeros(A)
printMatrix(A, 4)
