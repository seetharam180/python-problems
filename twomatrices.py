def add_matrices(matrix1, matrix2):
    if not matrix1 or not matrix2 or len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Incompatible matrix dimensions")

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result
matrix1=[[1,2,3],[4,5,6],[7,8,9]]
matrix2=[[1,2,3],[4,5,6],[7,8,9]]
print(add_matrices(matrix1,matrix2))


        