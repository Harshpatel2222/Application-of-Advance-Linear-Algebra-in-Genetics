from printMatrix import*
from MatrixMultiplication import*
from MatrixInverse import*
from eigenVectors import*
from diagonalMatrix import*
import matplotlib.pyplot as plt

print("Enter initial frequency of flower of genotypes AA: ")
a_0 = float(input())
print("Enter initial frequency of flower of genotypes Aa: ")
b_0 = float(input())
print("Enter initial frequency of flower of genotypes aa: ")
c_0 = float(input())

print("Enter Generation for which you wanted to count: ")
gen = int(input())

print(''' Select any any 3 genotypes pair which you want to fertilize: 
1. AA,AA
2. Aa,Aa
3. aa,aa
4. Aa,AA
5. Aa,aa
6. AA,aa''')

n = []
a = [[],
     [],
     []]

for j in range(0, 3):
    x = int(input())
    n.append(x)
    i=0
    if n[j] == 1:
        a[i].append(1)
        a[i+1].append(0)
        a[i+2].append(0)
    elif n[j] == 2:
        a[i].append(.25)
        a[i+1].append(.5)
        a[i+2].append(.25)
    elif n[j] == 3:
        a[i].append(0)
        a[i+1].append(0)
        a[i+2].append(1)
    elif n[j] == 4:
        a[i].append(.5)
        a[i+1].append(.5)
        a[i+2].append(0)
    elif n[j] == 5:
        a[i].append(0)
        a[i+1].append(1)
        a[i+2].append(0)
    elif n[j] == 6:
        a[i].append(0)
        a[i+1].append(.5)
        a[i+2].append(.5)



PrintMatrix(a,3,3)

eig_values=[0,0,0]
eig_values[0],eig_values[1],eig_values[2] = (get_eigenValues(a))

D = get_diagonalMatrix(eig_values)

P = get_eigenVectors(a,3)

N=D
for i in range(1,gen):
    N = matrixMultiplaction(N,D)

P_ = getMatrixInverse(P)
f = matrixMultiplaction(N,P_)
f = matrixMultiplaction(P,f)

x = [[a_0],[b_0],[c_0]]
ans = matrixMultiplaction(f,x)

print("After {0}th generation genotype distribution of AA: {1}".format(gen,"{:.2f}".format(ans[0][0])))
print("After {0}th generation genotype distribution of Aa: {1}".format(gen,"{:.2f}".format(ans[1][0])))
print("After {0}th generation genotype distribution of aa: {1}".format(gen,"{:.2f}".format(ans[2][0])))


#For plotting Pie Chart
# Data to plot
labels = 'AA', 'Aa', 'aa'
sizes = [a_0,b_0,c_0]
colors = ['gold', 'yellowgreen', 'lightcoral']
explode = (0, 0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()

# Data to plot
labels = 'AA', 'Aa', 'aa'
sizes = [ans[0][0],ans[1][0],ans[2][0]]
colors = ['gold', 'yellowgreen', 'lightcoral']
explode = (0, 0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()






'''
import numpy as np

#M = np.array([[[a[0], a[1], a[2]], [b[0], b[1], b[2]], [c[0], c[1], c[2]]]])
#print(M)
from numpy import linalg as LA

eigval, eigvec = LA.eig(M)
# print(eigval)
#print(eigvec)
p = eigvec
p_i = LA.inv(p)

d = np.diag(eigval[0])
# print(d)
from numpy.linalg import matrix_power

d_p=matrix_power(d, gen)


y = np.dot(p,d_p)
x = np.dot(y, p_i)
#print(x)

x_0 = np.array([[[a_0],[b_0],[c_0]]])
#print(x_0)

f = np.dot(x,x_0)
#print(f)

a_n = float(f[0][0])
b_n = float(f[0][1])
c_n = float(f[0][2])

print("Value of AA after {0}th generation is: ".format(gen),end='')
print("{:.2f}".format(a_n))

print("Value of Aa after {0}th generation is: ".format(gen),end='')
print("{:.2f}".format(b_n))

print("Value of aa after {0}th generation is: ".format(gen),end='')
print("{:.2f}".format(c_n))



'''