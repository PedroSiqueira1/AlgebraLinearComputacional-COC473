def forward_substitution(matrix_lu, vector_b):
    y = []

    for i in range(len(vector_b)):
        summ = 0
        for j in range(i-1):
            summ += matrix_lu[i][j] * y[j]

        y[i] = (b[i] - summ)/matrix_lu[i][i]

    return y



def backward_substitution():

    return 



def pivot(matrix_a, line):
    for k in range(line, len(matrix_a)):
        if matrix_a[k][line] != 0:
            temp = matrix_a[line]
            matrix_a[line] = matrix_a[k]
            matrix_a[k] = temp
    
    return matrix_a