import numpy as np
import operations as op

def get_jacobian(vector_x):

    def f1_gradient(vector_x):
        c2 = vector_x[0]
        c3 = vector_x[1]
        c4 = vector_x[2]
                            # 2*c3^2    + c2^2      + 6*c4^2

        gradient_c2 = 2*c2  # 0         + 2*c2      + 0
        gradient_c3 = 4*c3  # 4*c3      + 0*(c2^2)  + 0
        gradient_c4 = 12*c4 # 0         + 0*(c2^2)  + 12*c4

        vector_answer =  [gradient_c2, gradient_c3, gradient_c4]
        return vector_answer


    def f2_gradient(vector_x):
        c2 = vector_x[0]
        c3 = vector_x[1]
        c4 = vector_x[2]
                                                                # 8*c3^3    + 6*c3*c2^2 + 36*c3*c2*c4   + 108*c3*c4^2

        gradient_c2 = 12*c3*c2 + 36*c3*c4                       # 0         + 12*c3*c2  + 36*c3*c4      + 0
        gradient_c3 = 24*c3^2 + 6*c2^2 + 36*c2*c4 + 108*c4**2   # 3*8*c3^2  + 6*c2^2    + 36*c2*c4      + 108*c4^2
        gradient_c4 = 36*c3*c2 + 216*c3*c4                      # 0         + 0         + 36*c3*c2      + 216*c3*c4

        vector_answer =  [gradient_c2, gradient_c3, gradient_c4]
        return vector_answer


    def f3_gradient(vector_x):
        c2 = vector_x[0]
        c3 = vector_x[1]
        c4 = vector_x[2]
                                                                                                                # 60*c3^4   + 60*c3^2*c2^2  + 576*c3^2*c2*c4    + 2232*c3^2*c4^2  + 252*c4^2*c2^2   + 1296*c4^3*c2      + 3348*c4^4     + 24*c2^3*c4    + 3*c2

        gradient_c2 = 120*c3*c3*c2 + 576*c3*c3*c4 + 504*c4*c4*c2 + 1296*c4*c4*c4 + 72*c2*c2*c4 + 3              # 0         + 2*60*c3^2*c2  + 576*c3^2*c4       + 0               + 2*252*c4^2*c2   + 1296*c4^3         + 0             + 3*24*c2^2*c4  + 3
        gradient_c3 = 4*60*c3*c3*c3   + 2*60*c3*c2*c2   + 2*576*c3*c2*c4 + 4464*c3*c4*c4                        # 4*60*c3^3 + 2*60*c3*c2^2  + 2*576*c3*c2*c4    + 2*2232*c3*c4^2  + 0               + 0                 + 0             + 0             + 0
        gradient_c4 = 576*c3*c3*c2 + 4464*c3*c3*c4  + 504*c4*c2*c2 + 3888*c4*c4*c2  + 13392*c4*c4*c4 + 24*c2*c2 # 0         + 0             + 576*c3^2*c2       + 2*2232*c3^2*c4  + 2*252*c4*c2^2   + 3*1296*c4^2*c2    + 4*3348*c4^3   + 24*c2^3       + 0

        vector_answer =  [gradient_c2, gradient_c3, gradient_c4]
        return vector_answer


    jacobian = [ f1_gradient(vector_x), f2_gradient(vector_x), f3_gradient(vector_x) ]

    return jacobian

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






