#eigenValues.py

def get_eigenValues(M):
    a = -1
    b = M[0][0]+M[1][1]+M[2][2]
    c = -(M[0][0]*M[1][1] + M[0][0]*M[2][2] + M[1][1]*M[2][2] - M[0][1]*M[1][0] - M[0][2]*M[2][0] - M[2][1]*M[1][2])
    d = M[0][0]*M[1][1]*M[2][2] - M[0][0]*M[2][1]*M[1][2] + M[0][1]*M[2][0]*M[1][2] - M[0][1]*M[1][0]*M[2][2] + M[0][2]*M[1][0]*M[2][1] - M[0][2]*M[2][0]*M[1][1]

    f = ((3 * c / a) - (pow(b, 2) / pow(a, 2))) / 3
    # print(f)

    g = ((2 * pow(b, 3) / pow(a, 3)) - (9 * b * c / pow(a, 2)) + (27 * d / a)) / 27
    # print(g)

    h1 = (pow(g, 2) / 4) + (pow(f, 3) / 27)
    # print(h)

    h = (round(h1, 10))
    eig_values=[]

    import math

    if h <= 0:
        i = math.sqrt((pow(g, 2) / 4) - h)
        j = pow(i, 1 / 3)
        k = math.acos(-(g / (2 * i)))
        L = j * (-1)
        M = math.cos(k / 3)
        N = math.sqrt(3) * math.sin(k / 3)
        P = (b / (3 * a)) * (-1)

        x1 = (2 * j) * math.cos(k / 3) - (b / (3 * a))
        x3 = (L * (M + N)) + P
        x2 = (L * (M - N)) + P
        eig_values.append(round(x1,3))
        eig_values.append(round(x2,3))
        eig_values.append(round(x3,3))
        return eig_values[0],eig_values[1],eig_values[2]
    elif h > 0:
        R = (-g / 2) + math.sqrt(h)
        S = pow(R, 1 / 3)
        T = (-g / 2) - math.sqrt(h)
        U = pow(T, 1 / 3)
        x1 = (S + U) - (b / (3 * a))
        eig_values.append(round(x1,3))
        return eig_values[0]

    elif f == 0 and g == 0 and h == 0:
        x1 = x2 = x3 = pow((d / a), 1 / 3) * (-1)
        eig_values.append(round(x1, 3))
        eig_values.append(round(x2, 3))
        eig_values.append(round(x3, 3))
        return eig_values[0],eig_values[1],eig_values[2]