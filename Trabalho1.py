import numpy as np

A = np.array([[1,2,2]
             ,[4,4,2]
             ,[4,6,4]],float)


def gauss_elimination(A):
    """Função que recebe uma matriz e retorna ela escalonada"""

    for i in range(0, len(A)): 
        for j in range(i+1, len(A)):
            for k in range(i, len(A)): 
                print((A[j][i] / A[i][i]), j,k)

                A[j][k] = A[j][k] - (A[j][i] / A[i][i]) * A[i][k]
                
    return A
print(gauss_elimination(A))
def solve_equation(N = 0, ICOD = 1, IDET = 0, A = 0, B = 0, TolM = 0):

    if (ICOD == 1): # Decomposição LU   

        L = np.identity() # Define L como matriz identidade

        # Transformação de A em U
        
        for i in range(0, len(A)):
            for j in range(i+1, len(A)):
                A[j][i] = A[j][i] / A[i][i]
            for k in range(i+1, len(A)):
                for l in range(i+1, len(A)):
                    A[l][k] = A[l][k] - A[l][i] * A[i][k]
        

        return L , U

    if (ICOD == 2): # Decomposição de Cholesky
        pass
    if (ICOD == 3): # Método Jacobi
        pass
    if (ICOD == 4): # Método Gauss-Seidel
        pass

    return 0

