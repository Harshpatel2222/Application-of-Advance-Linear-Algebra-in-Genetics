# MatrixDeterminant.py

def getMatrixMinor(M,i,j):
    return [row[:j] + row[j+1:] for row in (M[:i]+M[i+1:])]

# row in M[:i] + M[i+1:] gives first i row of M
# row[:j] + row[j+1:] gives all elements of row expect jth element

def getMatrixDeternminant(M):
    #base case for 2x2 matrix
    if len(M) == 2:
        return M[0][0]*M[1][1]-M[0][1]*M[1][0]

    determinant = 0
    for c in range(len(M)):
        determinant += ((-1)**c)*M[0][c]*getMatrixDeternminant(getMatrixMinor(M,0,c))
    return determinant