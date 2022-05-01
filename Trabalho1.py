import numpy as np
import operations as op

def verify_matrix(matrix): # verifies if the created matrix
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
    for line in range(len(matrix)):
        for column in range(0, line):
            if matrix[line][column] != matrix[column][line]:
                return False
    return True

matrix_a = np.array([[1,2,2]
             ,[4,4,2]
             ,[4,6,4]],float)

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



def solve_equation(N = 0, ICOD = 1, IDET = 0, matrix_a = 0, matrix_b = 0, TolM = 0.01):

    if (ICOD == 1): # Decomposição LU   
        # Transformação de matrix_a em LU
        for i in range(0, len(matrix_a)):
            for j in range(i+1, len(matrix_a)):
                if matrix_a[i][i] == 0:
                    matrix_a = op.pivot(matrix_a, i)

                matrix_a[j][i] = matrix_a[j][i] / matrix_a[i][i]
            for k in range(i+1, len(matrix_a)):
                for l in range(i+1, len(matrix_a)):
                    matrix_a[l][k] = matrix_a[l][k] - matrix_a[l][i] * matrix_a[i][k]
        
        matrix_b = op.forward_substitution(matrix_a,matrix_b)
        return op.backward_substitution(matrix_a,matrix_b)

    elif (ICOD == 2): # Cholesky decomposition
        for i in range(0,len(matrix_a)):
            summ = 0
            for k in range(0,i):
                summ += (matrix_a[i][k])**2
            matrix_a[i][i] = np.sqrt(matrix_a[i][i] - summ)
            for j in range(i+1,len(matrix_a)):
                summ = 0
                for k in range(0,i):
                    summ += (matrix_a[i][k] * matrix_a[j][k])
                matrix_a[j][i]  = (matrix_a[i][j] - summ)/matrix_a[i][i]
                matrix_a[i][j] = matrix_a[j][i]

        matrix_b = op.forward_substitution(matrix_a,matrix_b)
        return op.backward_substitution(matrix_a,matrix_b)
    elif (ICOD == 3): # Jacobi Method
        pass
    elif (ICOD == 4): # Gauss-Seidel Method
        pass

    else:
        print("Invalid ICOD")
    return 0
'''
A = np.array([[1,2,2]
   ,[4,4,2]
   ,[4,6,4]],float)
B = np.array([3,6,10],float)

print(solve_equation(matrix_a=A,matrix_b=B))
'''
A = np.array([[1,0.2,0.4]
            ,[0.2,1,0.5]
            ,[0.4,0.5,1]],float)
B = np.array([0.6,-0.3,-0.6],float)








