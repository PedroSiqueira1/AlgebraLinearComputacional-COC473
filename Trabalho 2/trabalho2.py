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
    return np.e**x
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
    delta_x = 10
    while (abs(delta_x) > tolM and iter < max_iter):
        
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
# gauss quadrature function
def gauss_quadrature(vector_c, a, b, n):
    length = b-a

    def app_fun(z):
        x = 1/2 * (a + b + z*length) # b-a is the length of the interval
        return apply_function(vector_c, x)

    all_weights = [
        [1.0, 1.0],
        [0.88888, 0.55555, 0.55555],
        [0.65215, 0.65215, 0.34786, 0.34786],
        [0.56888, 0.47863, 0.47863, 0.23693, 0.23693],
        [0.36076, 0.36076, 0.46791, 0.46791, 0.17132, 0.17132],
        [0.41795, 0.38183, 0.38183, 0.27971, 0.27971, 0.12948, 0.12948],
        [0.36268, 0.36268, 0.31370, 0.31370, 0.22238, 0.22238, 0.10123, 0.10123],
        [0.33024, 0.18065, 0.18065, 0.08127, 0.08127, 0.31235, 0.31235, 0.26061, 0.26061],
        [0.29552, 0.29552, 0.26927, 0.26927, 0.21909, 0.21909, 0.14945, 0.14945, 0.06667, 0.06667]
        ]

    all_points = [
        [-0.57735, 0.57735],
        [0.00000, -0.77460, 0.77460],
        [-0.33998, 0.33998, -0.86114, 0.86114],
        [0.00000, -0.53847, 0.53847, -0.90618, 0.90618],
        [0.66121, -0.66121, -0.23862, 0.23862, -0.93247, 0.93247],
        [0.00000, 0.40585, -0.40585, -0.74153, 0.74153, -0.94911, 0.94911],
        [-0.18343, 0.18343, -0.52553, 0.52553, -0.79667, 0.79667, -0.96029, 0.96029],
        [0.00000, -0.83603, 0.83603, -0.96816, 0.96816, -0.32425, 0.32425, -0.61337, 0.61337],
        [-0.14887, 0.14887, -0.43340, 0.43340, -0.67941, 0.67941, -0.86506, 0.86506, -0.97391, 0.97391],
        ]

    weights = np.array(all_weights[n-2])
    points = np.array(all_points[n-2])

    # integral = length/2 * sum(wi * f(xi))
    integral = 0
    for i in range(n):
        integral += weights[i] * app_fun(points[i])

    integral = (length/2) * integral

    return {"integral": integral}


def polynomial_quadrature(vector_c, a, b, n):
    length = b-a
    all_weights = [
        [length],
        [length/2, length/2],
        [length/6, 2*length/3, length/6],
        [length/8, 3*length/8, 3*length/8, length/8],
        [7*length/90, 16*length/45, 2**length/15, 16*length/45, 7*length/90],
        ]

    weight = np.array(all_weights[n-1])
    
    if n == 1:
        coordinates = np.array([(a+b)/2])
    else:
        cord_list = []
        step = (b-a)/(n-1)
        for count in range(n):
            cord_list.append(a + count*step)

        coordinates = np.array(cord_list)

    integral = 0
    for i in range(len(coordinates)):
        integral += weight[i] * apply_function(vector_c, coordinates[i])
    
    return {"integral": integral}


# DERIVATE 
def derivate(vector_c, a, b):
    f_a = apply_function(vector_c, a)
    f_b = apply_function(vector_c, b)
    derivate = (f_b - f_a) / (b - a)

    return {"derivate": derivate}

# DERIVATE RE
def derivate_re(vector_c, x, delta1, delta2):
    def app_fun(x):
        return apply_function(vector_c, x)
    
    d1 = (app_fun(x+delta1) - app_fun(x)) / delta1
    d2 = (app_fun(x+delta2) - app_fun(x)) / delta2
    q = delta1 / delta2
    p = 1

    derivate = d1 + ((d1 - d2)/((q**(-p)) - 1))

    return {"derivate": derivate}


def main(ICOD = 1, method = 0, vector_c = np.array([1.0, 1.0, 1.0]), a = 100, b = -100, n = 2, tolM=0.00001, max_iter=10000):
    
    if (ICOD == 1): # Find root
        
        if method == 0:
            answer_dict = bisection_method(vector_c, a, b, tolM)
            answer_dict["variables"] = {"vector_c": vector_c, "a": a, "b": b, "tolM": tolM}

        else:
            avg = (a + b) / 2
            answer_dict = newton_method(vector_c, avg, tolM, max_iter)
            answer_dict["variables"] = {"vector_c": vector_c, "avg": avg, "tolM": tolM, "max_iter": max_iter}

        return answer_dict
        

    if (ICOD == 2): # Integrate

        if method == 0: # Guass quadrature
            answer_dict = gauss_quadrature(vector_c, a, b, n)
            answer_dict["variables"] = {"vector_c": vector_c, "a": a, "b": b, "n": n}

        else: # Polynomial quadrature
            answer_dict = polynomial_quadrature(vector_c, a, b, n)
            answer_dict["variables"] = {"vector_c": vector_c, "a": a, "b": b, "n": n}

        return answer_dict

    
    if (ICOD == 3): # Derivate
        delta_x = b # Use b as Δx
        if method == 0: # step ahead
            step = a + delta_x
            answer_dict = derivate(vector_c, a, step)
            answer_dict["variables"] = {"vector_c": vector_c, "x1 [a]": a, "x2 [a+b]": step}

        elif method == 1: # step behind
            step = a - delta_x
            answer_dict = derivate(vector_c, step, a)
            print()
            answer_dict["variables"] = {"vector_c": vector_c, "x1 [a-b]": step, "x2 [a]": a}

        elif method == 2: # central
            step = (delta_x/2)
            x1 = a-step
            x2 = a+step
            answer_dict = derivate(vector_c, x1, x2)
            answer_dict["variables"] = {"vector_c": vector_c, "x1 [a-b/2]": x1, "x2 [a+b/2]": x2}

        return answer_dict

    if (ICOD == 4): # Deivate RE
        
        answer_dict = derivate_re(vector_c, a, b, n) # vector_c, x, /\1, /\2
        
        answer_dict["variables"] = {"vector_c": vector_c, "x [a]": a, "delta1 [b]": b, "delta2 [n]": n}
        return answer_dict
        
    print("Invalid ICOD")
    return {"error": "Invalid ICOD"}


print(main(ICOD=1, method=1, vector_c=np.array([1.0, 1.0, 1.0,1.0]), a=-20, b=30, n=3, tolM=0.00001, max_iter=1000000))
