import numpy as np
import operations as op

matrix_a = np.array([[1,2,2]
             ,[4,4,2]
             ,[4,6,4]],float)



def solve_equation(N = 0, ICOD = 1, IDET = 0, matrix_a = None, matrix_b = None, tolM = 0.001):

    if not op.verify_square(matrix_a):
        print("ERROR")

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
        
        matrix_b = op.forward_substitution(matrix_a, matrix_b, True)
        return op.backward_substitution(matrix_a, matrix_b)

    if (ICOD == 2): # Cholesky decomposition
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
    
    if (ICOD == 3): # Jacobi Method
        if not op.verify_symmetry(matrix_a):
            print("ERROR")
            return False
        
        pos, value = op.greater_jacobi(matrix_a)
        matrix_v = np.identity(len(matrix_a))
        while(value > tolM):
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

        # Considerando: AX = B
        # X = V A(-1) V(t) B
        print("\n ------ \n")
        print("V", matrix_v)
        print("A", matrix_a)
        print("B", matrix_b)

        matrix_a = op.inverse_diagonal(matrix_a) # A(-1) <= A
        matrix_a = np.matmul(matrix_v, matrix_a) # V A(-1)
        matrix_v = np.transpose(matrix_v) # V(t)
        matrix_a = np.matmul(matrix_a, matrix_v) # V A(-1) V(t)
        matrix_a = np.matmul(matrix_a, matrix_b) # V A(-1) V(t) B

        return matrix_a

    if (ICOD == 4): # Gauss-Seidel Method
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
                x_new[i] = (matrix_b[i] - summ)/matrix_a[i][i]

            residuo.append(np.linalg.norm(x_new - x_old)/np.linalg.norm(x_new))

            if (np.linalg.norm(x_new - x_old)/np.linalg.norm(x_new)) <= tolM: # Código interrompe se o resíduo for menor que a tolerância escolhida.
                break
            x_old = x_new.copy()
            
        return x_new, iter, residuo
    
    print("Invalid ICOD")
    return 0

'''
A = np.array([[1, 0.2, 0]
            ,[0.2, 1, 0.5]
            ,[0, 0.5, 1]],float)
B = np.array([1.2, 1.7, 1.5],float)

print(solve_equation(ICOD=3, matrix_a=A, matrix_b=B))
'''



