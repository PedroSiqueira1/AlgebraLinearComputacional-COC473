import numpy as np

import operations as op

class Matrix():
    matrix = None
    scope = None    # 'A', 'L' or 'U'
    size = (None, None)

    def __init__(self, matrix, scope='A'):
        def valid(matrix, scope): # verifies if the created matrix is valid
            # SCOPE
            if scope not in {'A', 'L', 'U'}:
                print(f"{scope} is an invalid scope, it should be: A, L or U")
                return False

            # MATRIX - Not empty + all lines must have the same width
            length = len(matrix)
            
            if (size == 0 or len(matrix[0]) == 0):
                print("Empty matrix")
                return False
            
            width = len(matrix[0])
            for c in range(1, length):
                if len(matrix[c]) != width:
                    print(f"Line {c} has {len(matrix[c])}, when it should have {width}")
                    return False

            return True


        if not valid(matrix, scope):
            print("ERROR - Invalid matrix")

        self.scope = scope
        self.matrix = matrix
        self.size = (len(matrix), len(matrix[0]))

    def get(self, line, column):
        if not(type(line) == type(column) == 'int'):
            print(f"Line and Column must be integers, line: {type(line)}, column: {type(column)}")
        if self.scope == 'A':
            return self.matrix[line][column]

        elif self.scope == 'U':
            if column > line:
                return 0

        elif self.scope == 'L':
            return 0


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
        pass
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