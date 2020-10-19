#PrintMatrix.py

def PrintMatrix(M,row,column):
    for i in range(0,row):                       #for row
        for j in range(0,column):                #for column
            print("{:.2f}".format(M[i][j]),end="  ")
        print()