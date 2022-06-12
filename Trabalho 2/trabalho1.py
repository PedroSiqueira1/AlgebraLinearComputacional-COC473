import numpy as np
import operations as op

def get_jacobian(vector_x):

    c2 = vector_x[0]
    c3 = vector_x[1]
    c4 = vector_x[2]

    def f1_gradient(c2, c3, c4):
                            # 2*c3^2    + c2^2      + 6*c4^2

        gradient_c2 = 2*c2  # 0         + 2*c2      + 0
        gradient_c3 = 4*c3  # 4*c3      + 0*(c2^2)  + 0
        gradient_c4 = 12*c4 # 0         + 0*(c2^2)  + 12*c4

        vector_answer =  [gradient_c2, gradient_c3, gradient_c4]
        return vector_answer


    def f2_gradient(c2, c3, c4):
                                                                # 8*c3^3    + 6*c3*c2^2 + 36*c3*c2*c4   + 108*c3*c4^2

        gradient_c2 = 12*c3*c2 + 36*c3*c4                       # 0         + 12*c3*c2  + 36*c3*c4      + 0
        gradient_c3 = 24*c3**2 + 6*c2**2 + 36*c2*c4 + 108*c4**2 # 3*8*c3^2  + 6*c2^2    + 36*c2*c4      + 108*c4^2
        gradient_c4 = 36*c3*c2 + 216*c3*c4                      # 0         + 0         + 36*c3*c2      + 216*c3*c4

        vector_answer =  [gradient_c2, gradient_c3, gradient_c4]
        return vector_answer


    def f3_gradient(c2, c3, c4):
                                                                                                                # 60*c3^4   + 60*c3^2*c2^2  + 576*c3^2*c2*c4    + 2232*c3^2*c4^2  + 252*c4^2*c2^2   + 1296*c4^3*c2      + 3348*c4^4     + 24*c2^3*c4    + 3*c2

        gradient_c2 = 120*c3*c3*c2 + 576*c3*c3*c4 + 504*c4*c4*c2 + 1296*c4*c4*c4 + 72*c2*c2*c4 + 3              # 0         + 2*60*c3^2*c2  + 576*c3^2*c4       + 0               + 2*252*c4^2*c2   + 1296*c4^3         + 0             + 3*24*c2^2*c4  + 3
        gradient_c3 = 4*60*c3*c3*c3   + 2*60*c3*c2*c2   + 2*576*c3*c2*c4 + 4464*c3*c4*c4                        # 4*60*c3^3 + 2*60*c3*c2^2  + 2*576*c3*c2*c4    + 2*2232*c3*c4^2  + 0               + 0                 + 0             + 0             + 0
        gradient_c4 = 576*c3*c3*c2 + 4464*c3*c3*c4  + 504*c4*c2*c2 + 3888*c4*c4*c2  + 13392*c4*c4*c4 + 24*c2*c2 # 0         + 0             + 576*c3^2*c2       + 2*2232*c3^2*c4  + 2*252*c4*c2^2   + 3*1296*c4^2*c2    + 4*3348*c4^3   + 24*c2^3       + 0

        vector_answer =  [gradient_c2, gradient_c3, gradient_c4]
        return vector_answer


    jacobian = np.array([f1_gradient(c2, c3, c4), f2_gradient(c2, c3, c4), f3_gradient(c2, c3, c4)])

    return jacobian
def apply_function(vector_x, theta1, theta2):

    c2 = vector_x[0]
    c3 = vector_x[1]
    c4 = vector_x[2]

    def function1(c2,c3,c4):
        return 2*(c3**2) + c2**2 + 6*(c4**2) - 1
    def function2(c2,c3,c4):
        return 8*(c3**3) + 6*c3*(c2**2) + 36*c3*c2*c4 + 108*c3*(c4**2) - theta1
    def function3(c2,c3,c4):
        return 60*(c3**4) + 60*(c3**2)*(c2**2) + 576*(c3**2)*c2*c4 + 2232*(c3**2)*(c4**2) + 252*(c4**2)*(c2**2) + 1296*(c4**3)*c2 + 3348*(c4**4) + 24*(c2**3)*c4 + (3*c2) - theta2

    vector_answer = np.array([function1(c2,c3,c4),function2(c2,c3,c4),function3(c2,c3,c4)])
    return vector_answer



def newton_method(theta1, theta2, tolm, maxiter):

    vector_x = np.array([1, 1, 1]) # Initial guess
    for _ in range(maxiter):
        jacobian = get_jacobian(vector_x)
        vector_F = apply_function(vector_x,theta1,theta2)
        delta_x = op.lu(op.invert_jacobian(jacobian), vector_F) # AX = B -> -Jacobian * delta_x = vector_F

        vector_x = vector_x + delta_x
        erro = np.linalg.norm(delta_x)/np.linalg.norm(vector_x)
        if (erro <= tolm):
            return vector_x
        vector_x = vector_x 
    print('Matriz não convergiu!')
    return vector_x

def broyden_method(theta1, theta2, tolm, maxiter):

    vector_x = np.array([1,1,1]) # Initial guess
    jacobian = np.identity(3) # Initial jacobian guess
    next_F = apply_function(vector_x, theta1, theta2)

    for _ in range(maxiter):
        jacobian = get_jacobian(vector_x)
        vector_F = next_F
        delta_x = op.lu(op.invert_jacobian(jacobian), vector_F) # AX = B -> -Jacobian * delta_x = vector_F

        vector_x = vector_x + delta_x
        erro = np.linalg.norm(delta_x)/np.linalg.norm(vector_x)
        if (erro <= tolm):
            return vector_x

        next_F = apply_function(vector_x, theta1, theta2)
        vector_y = next_F - vector_F
        # J = J + (Y - B*ΔX)*ΔXt / (ΔXt * ΔX)
        jacobian = jacobian + np.matmul((vector_y - np.matmul(jacobian, delta_x)), np.transpose(delta_x)) / np.matmul(np.transpose(delta_x), delta_x)

    print('Matriz não convergiu!')
    return vector_x    

    return 1


def main(ICOD = 1, theta1 = 0,theta2 = 0, tolM = 0.01, max_iter= 10000):
    
    if (ICOD == 1): # Newthon Method
        
        answer = newton_method(theta1, theta2, tolM, max_iter)
        
        return answer
        

    if (ICOD == 2): # Cholesky decomposition
        
        answer = broyden_method(theta1, theta2, tolM, max_iter)
        
        return answer
        
    print("Invalid ICOD")
    return 0



print(main(1))
print(main(2))

