#MatrixMultiplication.py

def matrixMultiplaction(M1,M2):
    if len(M1[0])==len(M2):
        #for creating matrix which dimension is equal to matrix which we get by multiplication
        result=[[0 for j in range(len(M2))] for i in range(len(M1[0]))]
        for i in range(len(M1)):

            for j in range(len(M2[0])):

                for k in range(len(M2)):
                    result[i][j] += M1[i][k] * M2[k][j]
        return result
    else:
        print("Multiplication is not possible.")






















'''     from printMatrix import PrintMatrix
        PrintMatrix(result, len(M2),len(M1[0]) )
        

'''