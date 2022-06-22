import numpy as np

def forward_substitution(matrix_l, vector_b, triangle=False):
    vector_y = np.zeros(len(vector_b), float) 
    for i in range(len(vector_b)):
        summ = 0
        for j in range(i):
            summ += matrix_l[i][j] * vector_y[j]

        if triangle:
            den = 1
        else:
            den = matrix_l[i][i]

        vector_y[i] = (vector_b[i] - summ)/den

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
            return {"success": True, "matrix_a": matrix_a }

    print("ERROR de pivotagem")
    return {"success": False}


# Jacobi

def greater_jacobi(matrix):
    greater_value = 0
    for line in range(1, len(matrix)):
        for column in range(0, line):
            value = abs(matrix[line][column])
            if value > greater_value:
                greater_value = value
                greater_pos = (line, column)
    return greater_pos, greater_value


# ----- VERIFY -----
def dominant_diagonal(matrix):
    size = len(matrix)
    for c in range(size): # diagonal
        summ = 0
        
        for i in range(size): # summ of line
            summ += abs(matrix[c][i])
        
        if summ >= 2*abs(matrix[c][c]):
            print("dominant_diagonal: Diagonal not dominant, line:", c)
            return False

        summ = 0
        for i in range(size): # summ of column
            summ += matrix[i][c]

        if summ >= 2*abs(matrix[c][c]):
            print("dominant_diagonal: Diagonal not dominant, column:", c)
            return False

    return True
    

def verify_square(matrix): # verifies if the matrix is square
    height = len(matrix)
    if height == 0 or len(matrix[0]) == 0:
        print("ERROR - verify_square - empty matrix")
        return False
    
    width = len(matrix[0])
    for c in range(1, height):
        if len(matrix[c]) != width:
            print(f"ERROR - verify_square - Line {c} has {len(matrix[c])}, when it should have {width}")
            return False

    return True


def verify_symmetry(matrix):
    for line in range(1, len(matrix)):
        for column in range(0, line):
            if matrix[line][column] != matrix[column][line]:
                # Not symmetric
                return False
    return True

def gauss_seidel(matrix_a, vector_b):
    print("gauss")
    print("matrix_a\n", matrix_a)
    print("vector_b\n", vector_b)

    x_old = np.full(len(matrix_a),1.0) # Vector full of 1
    x_new = np.full(len(matrix_a),2.0) # Vector full of 2
    iter = 0
    residuo = []
    while True:
        iter +=1
        if iter >= 10000: # Código interrompe se não convergir em 10000 iterações
            break
        for i in range(0,len(matrix_a)):
            summ = 0        
            for j in range(0,len(matrix_a)):
                if j != i:
                    summ += (matrix_a[i][j]) * (x_new[j])
            x_new[i] = (vector_b[i] - summ)/matrix_a[i][i]

        residuo.append(np.linalg.norm(x_new - x_old)/np.linalg.norm(x_new))

        if (np.linalg.norm(x_new - x_old)/np.linalg.norm(x_new)) <= 0.001: # Código interrompe se o resíduo for menor que a tolerância escolhida.
            break
        x_old = x_new.copy()
    print("gauss:", x_new)
    return x_new


def lu(matrix_a, vector_b):
    matrix_a_init = matrix_a
    vector_b_init = vector_b

    for i in range(0, len(matrix_a)):
        for j in range(i+1, len(matrix_a)):
            if matrix_a[i][i] == 0:
                pivot_result = pivot(matrix_a, i)

                if pivot_result["success"]:
                    matrix_a = pivot_result["matrix_a"]
                else:
                    return gauss_seidel(matrix_a_init, vector_b_init)

            matrix_a[j][i] = matrix_a[j][i] / matrix_a[i][i]
        for k in range(i+1, len(matrix_a)):
            for l in range(i+1, len(matrix_a)):
                matrix_a[l][k] = matrix_a[l][k] - matrix_a[l][i] * matrix_a[i][k]

    vector_b = forward_substitution(matrix_a, vector_b, True)

    vector_b = backward_substitution(matrix_a, vector_b)

    return vector_b

def invert_jacobian(matrix):
    matrix = np.array(matrix)
    for i in range(len(matrix)):
        matrix[i] = matrix[i] * -1
    return matrix