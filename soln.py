#soln.py

import random

def soln(a,n):
    x = [0, 0, 0, ]
    for i in range(n - 1, -1, -1):
        j = i
        if a[i][j] == 0:
            x[i] = random.randint(0,101)
        else:
            x[i] = 0
            for j in range(j + 1, n):
                x[i] = x[i] - ((a[i][j] * x[j]) / a[i][i])
    return x