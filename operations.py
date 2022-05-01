import numpy as np


def forward_substitution():
    
    return 0



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

print(backward_substitution(np.array([[1,2,2],[0,-4,-6],[0,0,-1]],float), np.array([3,-6,1],float)))

def pivot(A, n):
    for k in range(n, len(A)):
        if A[k][n] != 0:
            temp = A[n]
            A[n] = A[k]
            A[k] = temp
    
    return A