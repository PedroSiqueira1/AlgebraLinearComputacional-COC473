import numpy as np

import operations as op


def main(n=0, ICOD=1, IDET=0, matrix_a=None, tolM=0.00001):

    if not op.verify_square(matrix_a):
        print("ERROR")
        return {"log": "Matriz A não é quadrada"}
    if ICOD == 1:
        vector_x = np.full(len(matrix_a),1.0)
        lamb = 1
        r = 1

        iteracoes = 0
        while(r > tolM):
            iteracoes += 1
            vector_x = np.matmul(matrix_a, vector_x)
            print("vx:", vector_x)
            x_max = np.abs(vector_x).max()
            print("x_max", x_max)
            print("lamb", lamb)

            vector_x = vector_x/x_max
            r = abs(x_max - lamb)/abs(x_max)
            lamb = x_max

        
        return {"eigenvalues": lamb, "eigenvectors": vector_x, "iterations": iteracoes}

    if ICOD == 2: # Jacobi-Method
        if not op.verify_symmetry(matrix_a):
            print("ERROR - Matriz A não é simétrica")
            return {"log": "Matriz A não é simétrica"}

        pos, value = op.greater_jacobi(matrix_a)
        matrix_v = np.identity(len(matrix_a))
        iteracoes = 0
        while(value > tolM and iteracoes < 10000):
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
            matrix_a = np.matmul(matrix_a, matrix_p) # A P
            matrix_p = np.transpose(matrix_p) # P -> P(t)
            matrix_a = np.matmul(matrix_p, matrix_a) #  P(t) [A P]
            
            matrix_p = np.transpose(matrix_p) # P(t) -> P

            # V' = V P
            matrix_v = np.matmul(matrix_v , matrix_p)

            pos, value = op.greater_jacobi(matrix_a)

        determinant = 1
        eigenvalues = []

        for c in range(len(matrix_a)):
            eigenvalues.append(matrix_a[c][c])
            
        answer = {"eigenvalues": eigenvalues, "eigenvectors": matrix_v, "iterations": iteracoes}

        if(IDET > 0):
            determinant = 1
            for c in range(len(matrix_a)):
                determinant *= matrix_a[c][c]
             
            answer["determinant"] = determinant

    
        

        return answer
    
    print("Erro: ICOD inválido")
    return {"log": "ICOD inválido"}

