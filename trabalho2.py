import numpy as np

import operations as op


def main(n=0, ICOD=1, IDET=0, matrix_a=None, tolM=0.00001):
    
    if ICOD == 1:
        vector_x = np.full(len(matrix_a),1.0)
        lamb = 1
        r = 1

        iteracoes = 0
        while(r > tolM):
            iteracoes += 1
            vector_x = np.matmul(matrix_a, vector_x)
            x_max = np.abs(vector_x).max()

            vector_x = vector_x/x_max

            r = abs(x_max - lamb)/abs(x_max)
            lamb = x_max
        
        return lamb, vector_x, iteracoes

    if ICOD == 2: # Jacobi-Method
        if not op.verify_symmetry(matrix_a):
            print("ERROR")
            return False
        pos, value = op.greater_jacobi(matrix_a)
        matrix_v = np.identity(len(matrix_a))
        iteracoes = 0
        while(value > tolM):
            iteracoes += 1
            line = pos[0]
            column = pos[1]

            # Define phi
            if matrix_a[line][line] == matrix_a[column][column]:
                phi = np.pi/4

            else:
                tan = 2 * matrix_a[line][column]/(matrix_a[line][line] - matrix_a[column][column])
                phi = np.arctan(tan)/2
            
            # Define matrix P
            matrix_p = np.identity(len(matrix_a))
            
            matrix_p[column][column] = np.cos(phi)
            matrix_p[column][line] = (-1) * np.sin(phi)
            matrix_p[line][column] = np.sin(phi)
            matrix_p[line][line] = np.cos(phi)

            # A' = P(t) A P
            matrix_a = np.matmul(matrix_a, matrix_p)
            matrix_p = np.transpose(matrix_p) # P -> P(t)
            matrix_a = np.matmul(matrix_p, matrix_a)
            
            matrix_p = np.transpose(matrix_p) # P(t) -> P

            # V' = V P
            matrix_v = np.matmul(matrix_v , matrix_p)

            pos, value = op.greater_jacobi(matrix_a)
            

        # matrix_a -> Autovalores (na diag princ)
        # matrix_v -> Autovetores (nas colunas)

        print("\n ------ \n")
        print("V", matrix_v)
        print("A", matrix_a)

        return matrix_a, matrix_v, iteracoes
    
    print("Erro: ICOD inválido")
    return False

A = np.array([[1,0.2,0]
   ,[0.2,1,0.5]
   ,[0,0.5,1]],float)

print(main(matrix_a=A, ICOD=2))
