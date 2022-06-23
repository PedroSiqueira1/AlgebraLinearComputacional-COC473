import numpy as np
import operations as op

def apply_function(x1, x2, vector_a, vector_w):
    a1 = vector_a[0]
    a2 = vector_a[1]
    a3 = vector_a[2]

    w1 = vector_w[0]
    w2 = vector_w[1]
    w3 = vector_w[2]
    return 

def runge_kutta_nystrom(tempo_total, h, tn, n,  vector_a, vector_w):
    def f_derivada(t, x, dx): # returns dxx aka x''
        a1 = vector_a[0]
        a2 = vector_a[1]
        a3 = vector_a[2]

        w1 = vector_w[0]
        w2 = vector_w[1]
        w3 = vector_w[2]

        return a1*np.sin(w1*t) + a2*np.sin(w2*t) + a3*np.cos(w3*t)
    
    def f_normal(t): # returns f(t)?
        a1 = vector_a[0]
        a2 = vector_a[1]
        a3 = vector_a[2]

        w1 = vector_w[0]
        w2 = vector_w[1]
        w3 = vector_w[2]

        return a1*np.sin(w1*t) + a2*np.sin(w2*t) + a3*np.cos(w3*t)
    

    n_steps = tempo_total/h
    t = 0.0
    dx = x = 0.0 # y'(0) = y(0) = 0.0

    for _ in range(n_steps):

        k1 = h * f_derivada(t, x, dx)
        q = 0.5*h * (dx + 0.5*k1)

        k2 = 0.5*h * f_derivada((t+h/2), (x+q), (dx+k1))

        k3 = 0.5*h * f_derivada((t+h/2), (x+q), (dx+k2))
        l = h * (dx + k3)
        
        k4 = 0.5*h * f_derivada((t+h), (x+l), (dx+ 2*k3))

        x = x + h*(dx + 1/3*(k1 + k2 + k3))
        dx = dx + 1/3*(k1 + 2*k2 + 2*k3 + k4)

        t = t + h
    
    return {"x": x}

def main(passo=1, tempo_total=10, m=1, c=0.1, k=2, vector_a=np.array([1.0, 2.0, 1.5]), vector_w=np.array([0.05, 1.0, 2.0])):
    
    answer = runge_kutta_nystrom(tempo_total, passo, vector_a, vector_w)

    return {"error": answer}



