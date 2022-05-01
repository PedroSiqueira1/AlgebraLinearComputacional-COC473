import numpy as np

def forward_substitution(matrix_l, vector_b):
    y = np.zeros(len(vector_b), float) 
    for i in range(len(vector_b)):
        summ = 0
        for j in range(i):
            summ += matrix_l[i][j] * y[j]   
        y[i] = (vector_b[i] - summ) #/matrix_l[i][i])


    return y

def backward_substitution(matrix_a,vector_b):
    number_of_rows = len(matrix_a)
    vector_x = np.zeros(len(vector_b),float)
    vector_x[-1] = vector_b[-1] / matrix_a[-1][-1]
    for i in range(len(matrix_a) - 1, -1, -1):   
        summ = 0
        for j in range(i+1,len(matrix_a)):
            summ+= matrix_a[i][j] * vector_x[j]
        vector_x[i] = (vector_b[i] - summ)/(matrix_a[i][i])
    return vector_x


def pivot(matrix_a, line):
    for k in range(line, len(matrix_a)):
        if matrix_a[k][line] != 0:
            temp = matrix_a[line]
            matrix_a[line] = matrix_a[k]
            matrix_a[k] = temp
    
    return matrix_a