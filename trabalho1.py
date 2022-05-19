import numpy as np
import operations as op

def main(N = 0, ICOD = 1, IDET = 0, matrix_a = None, matrix_b = None, tolM = 0.001):
    determinant = None
    if not op.verify_square(matrix_a):
        print("ERROR")
        return {"log": "Matriz A não é quadrada"}

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

        matrix_b = op.backward_substitution(matrix_a, matrix_b)

        answer = {"vectorX": matrix_b}

        if(IDET > 0):
            determinant = 1
            for i in range(0,len(matrix_a)):
                determinant *= matrix_a[i][i]
            
            answer["determinant"] = determinant

        return answer

    if (ICOD == 2): # Cholesky decomposition
        if not op.verify_symmetry(matrix_a):
            return {"log": "Matriz A não é simétrica"}

        for i in range(0,len(matrix_a)):
            summ = 0
            for k in range(0,i):
                summ += (matrix_a[i][k])**2

            if (matrix_a[i][i] - summ) < 0: # verification
                print("Invalid Matrix for Cholesky method")
                return {"log": "Matriz A não é positiva definida"}


            matrix_a[i][i] = np.sqrt(matrix_a[i][i] - summ)
            for j in range(i+1,len(matrix_a)):
                summ = 0
                for k in range(0,i):
                    summ += (matrix_a[i][k] * matrix_a[j][k])
                matrix_a[j][i]  = (matrix_a[i][j] - summ)/matrix_a[i][i]
                matrix_a[i][j] = matrix_a[j][i]

        matrix_b = op.forward_substitution(matrix_a,matrix_b)
        matrix_b = op.backward_substitution(matrix_a,matrix_b)
        
        answer = {"vectorX": matrix_b}
        
        if(IDET > 0):
            determinant = 1
            for i in range(0,len(matrix_a)):
                determinant *= matrix_a[i][i]
            determinant = determinant**2

            answer["determinant"] = determinant

        return answer
        
    
    if (ICOD == 3): # Jacobi Method
        if not op.verify_symmetry(matrix_a):
            print("ERROR - Matrix not symmetric")
            return {"log": "ERROR - Matrix not symmetric"}

        if not op.dominant_diagonal(matrix_a):
            print("ERROR - Matrix diagonal not dominant")
            return {"log": "ERROR - Matrix diagonal not dominant"}

        vector_x = np.full(N, 1.0)
        new_vector_x = np.full(N, 1.0)
        iter = 0
        residuo = 100
        while(residuo > tolM and iter < 10000):
            iter += 1
            for i in range(N):
                summ = 0
                for j in range(N):
                    if j != i:
                        summ += matrix_a[i][j] * vector_x[j]

                new_vector_x[i] = (matrix_b[i] - summ)/matrix_a[i][i]
            
            # calculating residuo - R = |X' - X| / |X'|
            abs_vec_x = pre_residuo = 0
            for c in range(N):
                pre_residuo += (new_vector_x[c] - vector_x[c])**2 # |X' - X|
                abs_vec_x += new_vector_x[c]**2 # |X'|

            residuo = np.sqrt(pre_residuo/abs_vec_x)

            vector_x = new_vector_x.copy()
        

        answer = {"vectorX": vector_x, "iterations": iter}
        
        if(IDET > 0):
            answer["determinant"] = "Não é possivel calcular o determinante para este método"

        return answer

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
            
        return {"vectorX": x_new, "iterations": iter, "residuo": residuo}
    
    print("Invalid ICOD")
    return 0






