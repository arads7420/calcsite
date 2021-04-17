import numpy as np
from numpy import linalg as LA
from sympy import *

#Multiply two 2x2 matrices
def multiply2x2matrices(a, b): 
    try:
        c = [[0, 0], [0, 0], [0, 0]]
        row1 = len(a)
        col1 = len(a[0])
        col2 = len(b[0])

        for i in range(0, row1):
            for j in range(0, col2):
                for k in range(0, col1):
                    c[i][j] += a[i][k] * b[k][j]

        return c
    except:
        error = {
            'error': 'Input is invalid'
        }
        return error

#Multiply two 3x3 matrices
def multiply3x3matrices(a, b): 
    try:
        c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        row1 = len(a)
        col1 = len(a[0])
        col2 = len(b[0])

        for i in range(0, row1):
            for j in range(0, col2):
                for k in range(0, col1):
                    c[i][j] += a[i][k] * b[k][j]

        return c
    except:
        error = {
            'error': 'Input is invalid'
        }
        return error
        

#Multiply two 4x4 matrices
def multiply4x4matrices(a, b): 
    try:
        c = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        row1 = len(a)
        col1 = len(a[0])
        col2 = len(b[0])

        for i in range(0, row1):
            for j in range(0, col2):
                for k in range(0, col1):
                    c[i][j] += a[i][k] * b[k][j]

        return c
    except:
        error = {
            'error': 'Input is invalid'
        }
        return error
        

#Add two 2x2 matrices
def add2x2matrices(a, b): 
    try:
        c = [[0, 0], [0, 0]]
        for i in range(0, len(a)):
            for j in range(0, len(a)):
                c[i][j] += a[i][j] + b[i][j]
                print(i, j)
        return c

    except:
        error = {
            'error': 'Invalid input'
        }
        return error

#Add two 3x3 matrices
def add3x3matrices(a, b): 
    try:
        c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(0, len(a)):
            for j in range(0, len(a)):
                c[i][j] += a[i][j] + b[i][j]
                print(i, j)
        return c

    except:
        error = {
            'error': 'Invalid input'
        }
        return error

#Add two 4x4 matrices
def add4x4matrices(a, b): 
    try:
        c = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        for i in range(0, len(a)):
            for j in range(0, len(a)):
                c[i][j] += a[i][j] + b[i][j]
                print(i, j)
        return c

    except:
        error = {
            'error': 'Invalid input'
        }
        return error

#Add two 5x5 matrices
def add5x5matrices(a, b): 
    try:
        c = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        for i in range(0, len(a)):
            for j in range(0, len(a)):
                c[i][j] += a[i][j] + b[i][j]
                print(i, j)
        return c

    except:
        error = {
            'error': 'Invalid input'
        }
        return error

def determinant2x2(a):
    try:
        det = a[0][0] * a[1][1] - a[0][1] * a[1][0]
        return det
    except:
        error = {
            'error': 'Invalid input'
        }
        return error

def determinant3x3(a):
    try:
        arr = np.array(a)
        det = np.linalg.det(arr)
        return np.around(det, decimals=2)
    except:
        error = {
            'error': 'Invalid input'
        }
        return error

def eigenvalues2x2(a):
    try:
        mat = Matrix(a)
        vec = mat.eigenvects()
        
        #Store the characteristic equation
        lamda = symbols('lambda')
        p = mat.charpoly(lamda)
        poly = latex(p.as_expr())

        #Convert Sympy matrix to list
        vec[0][2][0] = vec[0][2][0].tolist()
        vec[1][2][0] = vec[1][2][0].tolist()

        #Store Eigen Values in val_1 and val_2 
        val_1 = latex(vec[0][0])
        val_2 = latex(vec[1][0])

        #Store multiplicity
        m_1 = vec[0][1]
        m_2 = vec[1][1]

        #First Eigen Vector
        vec1_1 = latex(vec[0][2][0][0][0])
        vec1_2 = latex(vec[0][2][0][1][0])

        #Second Eigen Vector
        vec2_1 = latex(vec[1][2][0][0][0])
        vec2_2 = latex(vec[1][2][0][1][0])

        # print("eigen vector: ", vec[0][2][0].tolist())
        return {
            'val_1': val_1,
            'val_2': val_2,
            'm_1': m_1,
            'm_2': m_2,
            'vec1_1': vec1_1,
            'vec1_2': vec1_2,
            'vec2_1': vec2_1,
            'vec2_2': vec2_2,
            'poly': poly
        }   
    except:
        error = {
            'error': 'Invalid input'
        }
        return error

# a = [[5, 4], [1, 2]]
# c = eigenvalues2x2(a)
# print(c['poly'])

def eigenvalues3x3(a):
    try:
        mat = Matrix(a)
        # vec = mat.eigenvects()

        # #Store the characteristic equation
        lamda = symbols('lambda')
        p = mat.charpoly(lamda)
        poly = latex(p.as_expr())

        A = np.array(a)
        w, v = LA.eig(A)

        for i in range(len(w)):
            w[i] = np.round(w[i], decimals=6)

        for i in range(len(w)):
            v[i] = np.round(v[i], decimals=6)
            
        return {
            'val_1': w[0],
            'val_2': w[1],
            'val_3': w[2],
            'm_1': 1,
            'm_2': 1,
            'm_3': 1,
            'vec1_1': v[0][0],
            'vec1_2': v[0][1],
            'vec1_3': v[0][2],
            'vec2_1': v[1][0],
            'vec2_2': v[1][1],
            'vec2_3': v[1][2],
            'vec3_1': v[2][0],
            'vec3_2': v[2][1],
            'vec3_3': v[2][2],
            'poly': poly
        }   
    except:
        error = {
            'error': 'Invalid input'
        }
        return error

a = [[13, 13, 3], [1, 53, 1], [3, 1, 1]]
c = eigenvalues3x3(a)
print(c)