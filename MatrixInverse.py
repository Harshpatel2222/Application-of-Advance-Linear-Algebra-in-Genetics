#MatrixInverse.py

from MatrixDeterminant import*

def transposeMatrix(M):
    for i in range(len(M)):
        for j in range(len(M)):
            if i<j:
                temp=M[i][j]
                M[i][j]=M[j][i]
                M[j][i]=temp
    return M


def getMatrixInverse(M):
    determinant = getMatrixDeternminant(M)
    #special case for 2x2 matrix:
    if len(M) == 2:
        return [[M[1][1]/determinant, -1*M[0][1]/determinant],
                [-1*M[1][0]/determinant, M[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(M)):
        cofactorRow = []
        for c in range(len(M)):
            minor = getMatrixMinor(M,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(M)):
        for c in range(len(M)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors