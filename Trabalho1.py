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
        if not op.verify_symmetry(matrix_a):
            print("ERROR")
        
        pos, value = op.greater_jacobi(matrix_a)
        matrix_x = np.identity(len(matrix_a))
        while(value > tolM):
            line = pos[0]
            column = pos[1]

            if matrix_a[line][line] == matrix_a[column][column]:
                phi = np.pi()

            else:
                angle = 2 * matrix_a[line][column]/(matrix_a[line][line] - matrix_a[column][column])
                phi = np.arctan(angle)/2
            
            matrix_p = np.identity(len(matrix_a))
            
            matrix_p[column][column] = np.cos(phi)
            matrix_p[column][line] = (-1) * np.sin(phi)
            matrix_p[line][column] = np.cos(phi)
            matrix_p[line][line] = np.sin(phi)

            # P(t) A P
            matrix_a = np.matmul(matrix_a, matrix_p)
            matrix_p = np.transpose(matrix_p) # p becomes it's transpose
            matrix_a = np.matmul(matrix_p, matrix_a)
            
            matrix_p = np.transpose(matrix_p) # p goes back to it's innitial form

            pos, value = op.greater_jacobi(matrix_a)



    elif (ICOD == 4): # Gauss-Seidel Method
        x_old = np.full(len(matrix_a),1.0) # Vector full of 1
        x_new = np.full(len(matrix_a),2.0) # Vector full of 2
        iter = 0
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

            if (np.linalg.norm(x_new - x_old)/np.linalg.norm(x_new)) <= tolM: # Código interrompe se o resíduo for menor que a tolerância escolhida.
                break
            x_old = x_new.copy()
            
        return x_new
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
A = np.array([[3,-1,-1]
            ,[-1,3,-1]
            ,[-1,-1,3]],float)
B = np.array([1,2,1],float)


print(solve_equation(matrix_a=A,matrix_b=B,ICOD=4))





