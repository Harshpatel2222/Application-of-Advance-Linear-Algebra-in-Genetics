#echlonForm.py

def echlon_form(a, n):
    for i in range(0, n):
        j = i
        flag = 1
        if a[i][j] == 0:
            for k in range(i + 1, n):
                if a[k][j] != 0:
                    flag = 1
                    for j in range(0, n):
                        temp = a[i][j]
                        a[i][j] = a[k][j]
                        a[k][j] = temp
                else:
                    flag = 0
        if flag == 0:
            continue

        x = a[i][j]

        for y in range(i + 1, n):
            if a[y][j] != 0:
                mul = a[y][j] / x
                for z in range(0, n):
                    a[y][z] = a[y][z] - (a[i][z] * mul)