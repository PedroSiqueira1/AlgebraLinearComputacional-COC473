import numpy as np
import operations as op

jacobiana_global = [
    [],
    [],
    []]

def newton_method(theta1,theta2,tolm, maxiter):

    x = 1
    for _ in range(maxiter):
        f_x = 0 # Função f no ponto x
        df_x = 0 # Derivada da função f no ponto x

        h = f_x/df_x
        x_new = x - h
        if (abs(x_new - x) <= xtol):
            return x_new
        x = x_new 
        
    return x_new

def broyden_method(theta1,theta2,tolm):

    for c in range(1000):
        j = b

    return answer


def main(N = 0, ICOD = 1, IDET = 0, matrix_a = None, matrix_b = None, tolM = 0.001):
    determinant = None
    if not op.verify_square(matrix_a):
        print("ERROR")
        return {"log": "Matriz A não é quadrada"}

    if (ICOD == 1): # Newthon Method
        
        answer = newton_method()
        
        return answer
        

    if (ICOD == 2): # Cholesky decomposition
        
        answer = broyden_method()
        
        return answer
        
    print("Invalid ICOD")
    return 0






