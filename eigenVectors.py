#eigenvectors.py

from eigenValues import*
from soln import *
from echlonFrom import*

def get_eigenVectors(M,n):
    eig_values = get_eigenValues(M)
    y=[]
    for k in range(0,n):
        I = [[0 for j in range(n)] for i in range(n)]
        a = [[0 for j in range(n)] for i in range(n)]
        for i in range(0, n):
            for j in range(0, n):
                if i == j:
                    I[i][j] = 1
                else:
                    I[i][j] = 0
        for i in range(0,n):
            for j in range(0,n):
                I[i][j] = eig_values[k]*I[i][j]
        for i in range(0,n):
            for j in range(0,n):
                a[i][j] = M[i][j] - I[i][j]
        echlon_form(a,n)
        y.append(soln(a,n))
    eig_vectors = [[0 for j in range(0,n)] for i in range(0,n)]
    for i in range(0, 3):
        for j in range(0, 3):
            eig_vectors[i][j] = y[j][i]
    return eig_vectors














