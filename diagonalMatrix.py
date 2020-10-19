#diagonalMatrix.py

def get_diagonalMatrix(M):
    D = [[0 for j in range(len(M))] for i in range(len(M))]
    for i in range(0,len(M)):
        for j in range(0,len(M)):
            if i==j:
                D[i][j] = M[i]
            else:
                D[i][j] = 0
    return D