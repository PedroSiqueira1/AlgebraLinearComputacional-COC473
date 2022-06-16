import numpy as np
import operations as op



def derivate_function(vector_c, x):
    c1 = vector_c[0]
    c2 = vector_c[1]
    c3 = vector_c[2]
    c4 = vector_c[3]

    # f'(x) = c1 * e^(c2*x) + c3 * c4 * x^(c4-1)
    answer = c1 * np.exp(c2*x) + c3 * c4 * x**(c4 - 1)
    return answer

def apply_function(vector_c, x):

    c1 = vector_c[0]
    c2 = vector_c[1]
    c3 = vector_c[2]
    c4 = vector_c[3]

    # f(x) = c1 * e^(c2*x) + c3 * x^c4
    answer = c1 * np.exp(c2*x) + c3 * x**c4 
    return answer
    

# FIND ROOT
def bisection_method(vector_c, a, b, tolM):
    # local version of apply function
    def app_fun(x):
        return apply_function(vector_c, x)

    avg = (a + b) / 2
    f_a = app_fun(a) 
    f_b = app_fun(b)
    f_n = app_fun(avg)

    # VERIFY IF THE ROOT IS IN THE INTERVAL
    if (f_a > 0 and f_b > 0):
        print("ERROR - Não há raiz no intervalo fornecido")
        return {"error": "Não há raiz no intervalo fornecido"}

    elif (f_a < 0 and f_b < 0):
        print("ERROR -Não há raiz no intervalo fornecido")
        return {"error": "Não há raiz no intervalo fornecido"}

    # DO THE BISECTION METHOD
    iter = 0
    while (abs(a-b) > tolM):
        iter += 1

        if f_a > 0 and f_n > 0: # substitute a por avg
            a = avg
            f_a = app_fun(a)

        else: # substitute b por avg
            b = avg
            f_b = app_fun(b)

        avg = (a + b) / 2
        f_n = app_fun(avg)

    return {"root": avg, "iterations": iter}

def newton_method(vector_c, x, tolM, max_iter):

    iter = 0
    while (delta_x > tolM and iter < max_iter):
        iter += 1
        f_x = apply_function(vector_c, x)
        derivate = derivate_function(vector_c, x)

        delta_x = (-1) * f_x / derivate 

        x = x + delta_x
    

    answer = {"root": x, "iterations": iter}
    
    if (iter == max_iter):
        answer["error"] = "Max iterations reached"
    
    return answer


# INTEGRATE


# DERIVATE 
def derivate(vector_c, a, b):
    f_a = apply_function(vector_c, a)
    f_b = apply_function(vector_c, b)
    derivate = (f_b - f_a) / (b - a)

    return derivate

def main(ICOD = 1, method = 0, vector_c = np.array([1.0, 1.0, 1.0]), a = 100, b = -100, tolM=0.00001, max_iter=10000):
    
    if (ICOD == 1): # Find root
        
        if method == 0:
            answer_dict = bisection_method(vector_c, a, b, tolM)
        
        else:
            avg = (a + b) / 2
            answer_dict = newton_method(vector_c, avg, tolM, max_iter)
        
        return answer_dict
        

    if (ICOD == 2): # Integrate
        
        answer = "Not developed yet"
        
        return {"error": answer}
    
    if (ICOD == 3): # Derivate
        delta_x = b # Use b as Δx
        if method == 0: # step ahead
            step = a + delta_x
            answer = derivate(vector_c, a, step)

        elif method == 1: # step behind
            step = a - delta_x
            answer = derivate(vector_c, step, a)

        elif method == 2: # central
            step = (delta_x/2)
            x1 = a-step
            x2 = a+step
            answer = derivate(vector_c, x1, x2)
        
        return answer

    if (ICOD == 4): # Deivate RE
        
        answer = "Not developed yet"
        
        return {"error": answer}
        
    print("Invalid ICOD")
    return {"error": "Invalid ICOD"}



