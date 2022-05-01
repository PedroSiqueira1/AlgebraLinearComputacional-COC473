import numpy as np

def forward_substitution(matrix_l, vector_b, triangle=False):
    vector_y = np.zeros(len(vector_b), float) 
    for i in range(len(vector_b)):
        summ = 0
        for j in range(i):
            summ += matrix_l[i][j] * y[j]
        
        if triangle:
            den = 1
        else:
            den = matrix_l[i][i]

        vector_y[i] = (vector_b[i] - summ/den)

    return vector_y

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


# In: matrix_a -> Any matrix
# Out: The scalar of the matrix matrix_a 
def gauss_elimination(matrix_a):
    """Função que recebe uma matriz e retorna ela escalonada"""

    for i in range(0, len(matrix_a)): 
        for j in range(i+1, len(matrix_a)):
            for k in range(i, len(matrix_a)): 
                print((matrix_a[j][i] / matrix_a[i][i]), j,k)

                matrix_a[j][k] = matrix_a[j][k] - (matrix_a[j][i] / matrix_a[i][i]) * matrix_a[i][k]
                
    return matrix_a



def greater_jacobi(matrix):
    greater_value = 0
    for line in range(1, len(matrix)):
        for column in range(0, line):
            value = np.mod(matrix[line][column])
            if value > greater_value:
                greater_value = value
                greater_pos = (line, column)
    return greater_pos, greater_value

# ----- VERIFY -----
def verify_square(matrix): # verifies if the matrix is square
    height = len(matrix)
    if height == 0 or len(matrix[0]) == 0:
        print("Empty matrix")
        return False
    
    width = len(matrix[0])
    for c in range(1, height):
        if len(matrix[c]) != width:
            print(f"Line {c} has {len(matrix[c])}, when it should have {width}")
            return False

    return True


def verify_symmetry(matrix):
    for line in range(1, len(matrix)):
        for column in range(0, line):
            if matrix[line][column] != matrix[column][line]:
                return False
    return True